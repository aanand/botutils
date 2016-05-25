from __future__ import absolute_import
from __future__ import unicode_literals

import os

from .command import check_call
from .command import CalledProcessError


def make_gif(all_frames, destination, frame_rate, max_size=None):
    step = 1

    while True:
        frames = all_frames[::step]
        if len(frames) < 2:
            raise Exception(
                "Can't make a file small enough ({} frames, step = {})"
                .format(len(all_frames), step))

        modified_frame_rate = int(round(frame_rate / step))

        cmd = [
            'convert',
            '-loop', '0',
            '-delay', '1x{}'.format(modified_frame_rate),
            '-layers', 'Optimize',
        ]
        cmd += frames
        cmd.append(destination)

        try:
            check_call(cmd)
        except CalledProcessError:
            # it's possible `convert` ran out of memory and was killed, so try
            # again with fewer frames
            step += 1
            continue

        if max_size and os.stat(destination).st_size > max_size:
            step += 1
            continue

        return
