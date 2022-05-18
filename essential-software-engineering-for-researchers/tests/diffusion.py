def heat(u, nt, nx, alpha, L, tmax):
    """Calculate a numerical solution to the one-dimensional heat equation

    Args:
        u (List[float]): initial temperature distribution (and boundary conditions)
        nt (int): number of time steps
        nx (int): number of nodes in x direction
        alpha (float): thermal diffusivity (assumed constant i.e. homogeneous material)
        L (float): length of domain in x direction
        tmax (float): end time

    Returns:
        List[float]: final temperature distribution
    """

    dx = L / (nx - 1)
    dt = tmax / (nt - 1)

    for t in range(nt - 1):
        u = step(u, dx, dt, alpha)

    return u


def step(u, dx, dt, alpha):
    r = alpha * dt / dx**2
    if r > 0.5:
        raise Exception("Please ensure r <= 0.5.")

    return (
        # first element: index starts from empty, ends before second element
        u[:1]
        # middle elements
        + [
            r * u[i + 1] + (1 - 2 * r) * u[i] + r * u[i - 1]
            for i in range(1, len(u) - 1)
        ]
        # last element: index starts from last element, ends at last element
        + u[-1:]
    )
