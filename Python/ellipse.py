#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/6/18 12:40 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: ellipse.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt


class Solution:

    @staticmethod
    def plot_parallel(horizon_distance, vertical_distance):
        """

        :param horizon_distance: int
        :param vertical_distance: int
        :return: void Do not return anything. plot four lines
        """
        x = np.linspace(-10, 10, 1000)
        y = np.linspace(0, 0, 1000)
        plt.plot(x, y, 'r')
        plt.plot(x, y + horizon_distance, 'r')
        plt.plot(y, x, 'b')
        plt.plot(y + vertical_distance, x, 'b')
        plt.axis('equal')

    @staticmethod
    def plot_ellipse(f1, f2, c, horizon_distance, vertical_distance):
        """
        this function use coordinates of focuses and constant parameter to draw a ellipse
        :param f1: List[int]
        :param f2: List[int]
        :param c: int
        :return: void Do not return anything. plot the ellipse
        """
        # first test the coordinates is valid
        a1, b1, a2, b2 = f1[0], f1[1], f2[0], f2[1]
        if ((a1 == 0 or a1 == 6 and 0 <= b1 <= horizon_distance) or
                (b1 == 0 or b1 == 4 and 0 <= a1 <= vertical_distance)):
            if ((a2 == 0 or a2 == 6 and 0 <= b2 <= horizon_distance) or
                    (b2 == 0 or b2 == 4 and 0 <= a2 <= vertical_distance)):
                print("value is valid!")
            else:
                print("please set the focus on the line")
                return False
        else:
            print("please set the focus on the line")
            return False
        # Compute ellipse parameters
        a = c / 2
        # Semimajor axis
        x0 = (a1 + a2) / 2
        # Center x-value
        y0 = (b1 + b2) / 2
        # Center y-value
        f = np.sqrt((a1 - x0)**2 + (b1 - y0)**2)
        # Distance from center to focus
        # check validness
        if a**2 - f**2 < 0:
            print('{} is less than {}'.format(a, f))
            print("please input a valid C value")
            return False
        b = np.sqrt(a**2 - f**2)
        # Semiminor axis
        phi = np.arctan2((b2 - b1), (a2 - a1))
        # Angle between major axis and x-axis
        # Parametric plot in t
        resolution = 1000
        t = np.linspace(0, 2*np.pi, resolution)
        x = x0 + a * np.cos(t) * np.cos(phi) - b * np.sin(t) * np.sin(phi)
        y = y0 + a * np.cos(t) * np.sin(phi) + b * np.sin(t) * np.cos(phi)
        # Plot ellipse
        plt.plot(x, y)
        # Show foci
        point_x, point_y = [[a1, a2]], [[b1, b2]]
        for i in range(len(point_x)):
            plt.plot(point_x[i], point_y[i], linewidth=1.0, linestyle='--')
            plt.scatter(point_x[i], point_y[i], color='black')
        # plt.plot(a1, b1, 'o')
        # plt.plot(a2, b2, 'o')
        plt.axis('equal')


if __name__ == '__main__':
    sol = Solution()
    d_horizon, d_vertical = 4, 6
    sol.plot_parallel(d_horizon, d_vertical)
    # set the focus coordinates
    # check validness
    # set the distance between the parallel line
    # set x-axis and y-axis limit between (-20, 20)
    plt.xlim((-15, 15))
    plt.ylim((-15, 15))
    # set the axis
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    # some example
    sol.plot_ellipse([1, 4], [6, 2], 7, d_horizon, d_vertical)
    sol.plot_ellipse([0, 3], [3, 0], 8, d_horizon, d_vertical)
    sol.plot_ellipse([6, 1], [1, 0], 9, d_horizon, d_vertical)
    plt.grid()
    plt.show()
