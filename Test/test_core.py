# to run tests python3 -m unittest Test.test_core from root dir

import unittest
from unittest.case import TestCase

import PassiveComp.core as PassiveComp

import Test.Model.core as Model

e3 = [1.0, 2.2, 4.7]
e6 = [1.0, 1.5, 2.2, 3.3, 4.7, 6.8]
e12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
e24 = [1.0, 1.1, 1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.2, 2.4, 2.7, 3.0, 3.3, 3.6, 3.9, 4.3, 4.7, 5.1, 5.6, 6.2, 6.8, 7.5, 8.2, 9.1]
e48 = [1.0, 1.05, 1.1, 1.15, 1.21, 1.27, 1.33, 1.4, 1.47, 1.54, 1.62, 1.69, 1.78, 1.87, 1.96, 2.05, 2.15, 2.26, 2.37, 2.49, 2.61, 2.74, 2.87, 3.01, 3.16, 3.32, 3.48, 3.65, 3.83, 4.02, 4.22, 4.42, 4.64, 4.87, 5.11, 5.36, 5.62, 5.9, 6.19, 6.49, 6.81, 7.15, 7.5, 7.87, 8.25, 8.66, 9.09, 9.53]
e96 = [1.0, 1.02, 1.05, 1.07, 1.1, 1.13, 1.15, 1.18, 1.21, 1.24, 1.27, 1.3, 1.33, 1.37, 1.4, 1.43, 1.47, 1.5, 1.54, 1.58, 1.62, 1.65, 1.69, 1.74, 1.78, 1.82, 1.87, 1.91, 1.96, 2.0, 2.05, 2.1, 2.15, 2.21, 2.26, 2.32, 2.37, 2.43, 2.49, 2.55, 2.61, 2.67, 2.74, 2.8, 2.87, 2.94, 3.01, 3.09, 3.16, 3.24, 3.32, 3.4, 3.48, 3.57, 3.65, 3.74, 3.83, 3.92, 4.02, 4.12, 4.22, 4.32, 4.42, 4.53, 4.64, 4.75, 4.87, 4.99, 5.11, 5.23, 5.36, 5.49, 5.62, 5.76, 5.9, 6.04, 6.19, 6.34, 6.49, 6.65, 6.81, 6.98, 7.15, 7.32, 7.5, 7.68, 7.87, 8.06, 8.25, 8.45, 8.66, 8.87, 9.09, 9.31, 9.53, 9.76]
e192 = [1.0, 1.01, 1.02, 1.04, 1.05, 1.06, 1.07, 1.09, 1.1, 1.11, 1.13, 1.14, 1.15, 1.17, 1.18, 1.2, 1.21, 1.23, 1.24, 1.26, 1.27, 1.29, 1.3, 1.32, 1.33, 1.35, 1.37, 1.38, 1.4, 1.42, 1.43, 1.45, 1.47, 1.49, 1.5, 1.52, 1.54, 1.56, 1.58, 1.6, 1.62, 1.64, 1.65, 1.67, 1.69, 1.72, 1.74, 1.76, 1.78, 1.8, 1.82, 1.84, 1.87, 1.89, 1.91, 1.93, 1.96, 1.98, 2.0, 2.03, 2.05, 2.08, 2.1, 2.13, 2.15, 2.18, 2.21, 2.23, 2.26, 2.29, 2.32, 2.34, 2.37, 2.4, 2.43, 2.46, 2.49, 2.52, 2.55, 2.58, 2.61, 2.64, 2.67, 2.71, 2.74, 2.77, 2.8, 2.84, 2.87, 2.91, 2.94, 2.98, 3.01, 3.05, 3.09, 3.12, 3.16, 3.2, 3.24, 3.28, 3.32, 3.36, 3.4, 3.44, 3.48, 3.52, 3.57, 3.61, 3.65, 3.7, 3.74, 3.79, 3.83, 3.88, 3.92, 3.97, 4.02, 4.07, 4.12, 4.17, 4.22, 4.27, 4.32, 4.37, 4.42, 4.48, 4.53, 4.59, 4.64, 4.7, 4.75, 4.81, 4.87, 4.93, 4.99, 5.05, 5.11, 5.17, 5.23, 5.3, 5.36, 5.42, 5.49, 5.56, 5.62, 5.69, 5.76, 5.83, 5.9, 5.97, 6.04, 6.12, 6.19, 6.26, 6.34, 6.42, 6.49, 6.57, 6.65, 6.73, 6.81, 6.9, 6.98, 7.06, 7.15, 7.23, 7.32, 7.41, 7.5, 7.59, 7.68, 7.77, 7.87, 7.96, 8.06, 8.16, 8.25, 8.35, 8.45, 8.56, 8.66, 8.76, 8.87, 8.98, 9.09, 9.19, 9.31, 9.42, 9.53, 9.65, 9.76, 9.88]



class TestCreateSeries(unittest.TestCase):

    def test_happyPathE3compareToModel_shouldAssertEqual(self):
        self.assertEqual(e3,PassiveComp.createSeries(3))

    def test_happyPathE6compareToModel_shouldAssertEqual(self):
        self.assertEqual(e6,PassiveComp.createSeries(6))

    def test_happyPathE12compareToModel_shouldAssertEqual(self):
        self.assertEqual(e12,PassiveComp.createSeries(12))

    def test_happyPathE24compareToModel_shouldAssertEqual(self):
        self.assertEqual(e24,PassiveComp.createSeries(24))

    def test_happyPathE48compareToModel_shouldAssertEqual(self):
        self.assertEqual(e48,PassiveComp.createSeries(48))

    def test_happyPathE96compareToModel_shouldAssertEqual(self):
        self.assertEqual(e96,PassiveComp.createSeries(96))

    def test_happyPathE192compareToModel_shouldAssertEqual(self):
        self.assertEqual(e192,PassiveComp.createSeries(192))


class TestCalculateSeries(unittest.TestCase):

    def test_happyPathcompareToModel_E3Target3_shouldAssertEqual(self):
        eSeries = e3
        targetValue = 3.14
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 2.2, 3.2)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))

    def test_happyPathcompareToModel_E6Target6_shouldAssertEqual(self):
        eSeries = e6
        targetValue = 6.28
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 4.7, 6.2)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))

    def test_happyPathcompareToModel_E12Target8_shouldAssertEqual(self):
        eSeries = e12
        targetValue = 8.3
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 6.8, 8.3)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))

    def test_happyPathcompareToModel_E24Target9_shouldAssertEqual(self):
        eSeries = e24
        targetValue = 9
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 7.5, 9.0)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))

    def test_happyPathcompareToModel_E48Target6_shouldAssertEqual(self):
        eSeries = e48
        targetValue = 6.28
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.15, 5.11, 6.3)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))

    def test_happyPathcompareToModel_E96Target2_shouldAssertEqual(self):
        eSeries = e96
        targetValue = 2.465
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 1.47, 2.5)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))

    def test_happyPathcompareToModel_E192Target3_shouldAssertEqual(self):
        eSeries = e192
        targetValue = 3.14
        #modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 2.08, 3.1)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries,targetValue))
