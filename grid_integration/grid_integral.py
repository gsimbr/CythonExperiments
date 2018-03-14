import numpy as np
import time
import numba

EPS = 1e-3


def profile(fcn):
    def wrap(*args, **kwargs):
        start = time.time()
        ret = fcn(*args, **kwargs)
        end = time.time()
        print "Time elapsed for {}: {}".format(fcn.__name__, end-start)
        return end-start, ret

    return wrap


@profile
def gaussian_naive(grid, sigma_x, sigma_y, rho):
    rho = max([EPS, rho])
    covariance_matrix = np.array([[sigma_x**2, rho], [rho, sigma_y**2]])

    factor = 1.0/((2*np.pi)**2*np.linalg.det(covariance_matrix))
    ret_grid = np.exp(
        np.einsum("ijk,kl,ijl->ij", grid, covariance_matrix, grid))
    return factor*ret_grid


@profile
@numba.jit
def gaussian_naive_jit(grid, sigma_x, sigma_y, rho):
    rho = max([EPS, rho])
    covariance_matrix = np.array([[sigma_x**2, rho], [rho, sigma_y**2]])

    factor = 1.0/((2*np.pi)**2*np.linalg.det(covariance_matrix))
    ret_grid = np.exp(
        np.einsum("ijk,kl,ijl->ij", grid, covariance_matrix, grid))
    return factor*ret_grid


@profile
def gaussian_very_naive(grid, sigma_x, sigma_y, rho):
    rho = max([EPS, rho])
    covariance_matrix = np.array([[sigma_x ** 2, rho], [rho, sigma_y**2]])
    factor = 1.0 / ((2 * np.pi) ** 2 * np.linalg.det(covariance_matrix))
    ret_grid = np.zeros(grid.shape[:-1])
    for i in xrange(ret_grid.shape[0]):
        for j in xrange(ret_grid.shape[1]):
            ret_grid[i, j] = factor*np.exp(
                np.dot(np.dot(grid[i, j], covariance_matrix), grid[i, j]))

    return ret_grid


@profile
@numba.jit
def gaussian_very_naive_jit(grid, sigma_x, sigma_y, rho):
    rho = max([EPS, rho])
    covariance_matrix = np.array([[sigma_x ** 2, rho], [rho, sigma_y**2]])
    factor = 1.0 / ((2 * np.pi) ** 2 * np.linalg.det(covariance_matrix))
    ret_grid = np.zeros(grid.shape[:-1])
    for i in xrange(ret_grid.shape[0]):
        for j in xrange(ret_grid.shape[1]):
            ret_grid[i, j] = factor*np.exp(
                np.dot(np.dot(grid[i, j], covariance_matrix), grid[i, j]))

    return ret_grid


def main(points):
    a = np.linspace(-2, 2, points)
    b = np.linspace(-5, 5, points)

    xx, yy = np.meshgrid(a, b)

    grid = np.vstack((xx.flatten(), yy.flatten())).T.reshape(
        (xx.shape[0], xx.shape[1], 2))

    return grid


if __name__ == '__main__':
    no_points = 100
    grid = main(no_points)
    sigma_x = 0.3
    sigma_y = 0.1
    rho = 0
    time_1, ret_1 = gaussian_naive(grid, sigma_x, sigma_y, rho)
    time_2, ret_2 = gaussian_very_naive(grid, sigma_x, sigma_y, rho)
    for _ in xrange(2):
        time_3, ret_3 = gaussian_very_naive_jit(grid, sigma_x, sigma_y, rho)
        time_4, ret_4 = gaussian_very_naive_jit(grid, sigma_x, sigma_y, rho)
    np.testing.assert_allclose(ret_1, ret_2)

    print "Very naive vs naive: {} \% of very naive".format(100.0*time_1/time_2)
    print "Very naive jit vs very naive: {} \% of very naive".format(
        100.0 * time_1 / time_3)
    print "Naive jit vs very naive: {} \% of very naive".format(
        100.0 * time_1 / time_4)
