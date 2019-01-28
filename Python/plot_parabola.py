#! /Users/xiaotongli/anaconda3/bin/python
# -*- coding: utf-8 -*-
# @Time    : 12/27/18 6:24 PM
# @Author  : Xiaotong Li
# @School  : University of California, Santa Cruz
# @FileName: plot_parabola.py
# @Software: PyCharm
import math
import numpy as np
import matplotlib.pyplot as plt

class Parabola:
    def plot_dot(self, x, y, legend, mark):
        point_x, point_y = [[x], [y]]
        for i in range(len(point_x)):
            plt.scatter(point_x[i], point_y[i], label=legend, marker=mark)

    def plot_parabola(self, fx, fy, vx, vy):
        if vx == fx and vy == fy:
            print('the coordinates of Vertex and Focus cannot be same\n')
            print('Please input a effective coordinates')
            return False
        # compute the distance between focus and vertex
        distance = math.sqrt(pow(vx - fx, 2) + pow(vy - fy, 2))
        x = np.linspace(-15, 15, 1000)
        y = np.linspace(-15, 15, 1000)
        # there will be 5 situations
        # 1. vx = fx, parabola open to up
        # parabola equation based on vertex
        # (x - h)^2 = 4 * c * (y - k), which vertex coordinate is (h, k)
        if vx == fx and vy < fy:
            y_1 = (x - vx) * (x - vx)/(4*distance) + vy
            plt.plot(x, y_1, 'r')
        # 2. vx = fx, parabola open to down
        # equation is (x - h)^2 = - 4 * c * (y - k)
        elif vx == fx and vy > fy:
            y_2 = - (x - vx) * (x - vx)/(4*distance) + vy
            plt.plot(x, y_2, 'b')
        # 3. vy = fy, parabola open to right
        # equation is (y - k)^2 = 4 * c * (x - h)
        elif vy == fy and vx < fx:
            x_1 = (y - vy) * (y - vy)/(4*distance) + vx
            plt.plot(x_1, y, 'y')
        # 4. vy = fy, parabola open to left
        # equation is (y - k)^2 = - 4 * c * (x - h)
        elif vy == fy and vx > fx:
            x_2 = - (y - vy) * (y - vy)/(4*distance) + vx
            plt.plot(x_2, y, 'g')
        # 5. general case
        # parabola equation based on vertex
        else:
            # compute the slope of the line vertex-focus
            t = np.linspace(-15, 15, 1000)
            k = (fy - vy) / (fx - vx)
            # compute the angle between line and y-axis
            phi = np.arctan2(abs(vx - fx), abs(vy - fy))
            if fx < vx and fy > vy:
                theta = phi
            elif fx < vx and fy < vy:
                theta = np.pi - phi
            elif fx > vx and fy > vy:
                theta = -phi
            elif fx > vx and fy < vy:
                theta = phi - np.pi
            print('angle is {}'.format(theta*180/np.pi))
            # rotate_matrix = [[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]
            y_original = ((t - vx) * (t - vx)/(4*distance) + vy)
            x_5 = t * np.cos(theta) - ((t - vx) * (t - vx)/(4*distance) + vy) * np.sin(theta)
            y_5 = t * np.sin(theta) + ((t - vx) * (t - vx)/(4*distance) + vy) * np.cos(theta)
            plt.plot(t, y_original)
            plt.plot(x_5, y_5)
            # compute the distance between vertex and focus
            d = distance / np.sin(np.pi/2 - phi)
            # the line of vertex-focus
            y_vx = k * (x - vx) + vy
            # get the vertical line slope
            k_verti = - 1/k
            plt.plot(x, y_vx, linestyle='--')
            # a, b = -k_verti, 1
            # the line which vertical to the line vertex-focus
            if fy > vy:
                y_vx_verti = k_verti * (x - vx) + vy - d
                plt.plot(x, y_vx_verti)
            elif fy < vy:
                y_vx_verti = k_verti * (x - vx) + vy + d
                plt.plot(x, y_vx_verti)


if __name__ == '__main__':
    para = Parabola()
    focus_x, focus_y = 3, 3
    para.plot_dot(focus_x, focus_y, 'F', 'x')
    vertex_x, vertex_y = 0, 0
    para.plot_dot(vertex_x, vertex_y, 'V', '^')
    plt.legend()
    para.plot_parabola(focus_x, focus_y, vertex_x, vertex_y)
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
    plt.grid()
    plt.axis('equal')
    plt.show()