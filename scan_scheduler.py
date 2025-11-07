def scan_scheduler(queue, head_position, direction):
    """
    The 'Elevator' algorithm.
    - direction: 1 for 'up', -1 for 'down'
    """
    in_direction = [r for r in queue if (r.block_number - head_position) * direction >= 0]

    if in_direction:
        in_direction.sort(key=lambda r: abs(r.block_number - head_position))
        next_request = in_direction[0]
        return next_request, direction
    else:
        new_direction = -direction
        other_direction = [r for r in queue if (r.block_number - head_position) * new_direction >= 0]
        if not other_direction:
            return None, direction

        other_direction.sort(key=lambda r: abs(r.block_number - head_position))
        next_request = other_direction[0]
        return next_request, new_direction
