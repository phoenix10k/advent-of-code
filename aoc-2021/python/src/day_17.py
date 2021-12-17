from dataclasses import dataclass

def sign(i: int) -> int:
    if i < 0:
        return -1
    if i > 0:
        return 1
    return 0

@dataclass
class State:
    velx: int
    vely: int
    posx: int = 0
    posy: int = 0

    def run_step(self) -> "State":
        return State(
            self.velx - sign(self.velx),
            self.vely - 1,
            self.posx + self.velx,
            self.posy + self.vely,
        )


@dataclass
class Box:
    minx: int
    maxx: int
    miny: int
    maxy: int


def cmp_target(state: State, target: Box) -> tuple[int, int]:
    """return a tuple (x, y) of cmp result for the target, i.e. -1 if pos is < target min,
    0 if pos is inside the target zone, +1 if pos is > target max."""
    if state.posx < target.minx:
        x = -1
    elif state.posx > target.maxx:
        x = 1
    else:
        x = 0

    if state.posy < target.miny:
        y = -1
    elif state.posy > target.maxy:
        y = 1
    else:
        y = 0

    return x, y

def evaluate_case(velx: int, vely: int, target: Box ) -> tuple[int, tuple[int, int]]:
    """return tuple of max height and the stopping condition."""
    state = State(velx, vely)
    max_height = 0
    while True:
        state = state.run_step()
        max_height = max(max_height, state.posy)
        cmp_result = cmp_target(state, target)
        match cmp_result:
            case (0,0):
                return max_height, cmp_result
            case (-1, _):
                if state.velx == 0:
                    # undershot x
                    return -1, cmp_result
            case (1, _):
                # overshot x
                return -1, cmp_result
            case (_, -1):
                # undershot y
                return -1, cmp_result


def optimise_height(target: Box) -> tuple[State, int]:
    """return tuple of Initial state and max height for the optimal trajectory."""

    max_height = 0
    best_initial_state = State(0,0)
    for x in range(1,100):
        for y in range(1,200):
            height, cmp_result = evaluate_case(x, y, target)
            if cmp_result == (0, 0) and height > max_height:
                max_height = height
                best_initial_state = State(x, y)            
    
    return best_initial_state, max_height


if __name__ == "__main__":
    print("part 1:", optimise_height(Box(124, 174, -123, -86)))
