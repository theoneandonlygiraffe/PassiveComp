# to run tests python3 -m unittest Test.test_core from root dir

import unittest

import PassiveComp.core as PassiveComp
import Test.Model.eseries as model


class TestCreateSeries(unittest.TestCase):
    def test_happyPathE3compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_3, PassiveComp.createSeries(3))

    def test_happyPathE6compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_6, PassiveComp.createSeries(6))

    def test_happyPathE12compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_12, PassiveComp.createSeries(12))

    def test_happyPathE24compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_24, PassiveComp.createSeries(24))

    def test_happyPathE48compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_48, PassiveComp.createSeries(48))

    def test_happyPathE96compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_96, PassiveComp.createSeries(96))

    def test_happyPathE192compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_192, PassiveComp.createSeries(192))


class TestCalculateSeries(unittest.TestCase):
    def test_happyPathcompareToModel_E3Target3_shouldAssertEqual(self):
        eSeries = model.E_3
        targetValue = 3.14
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 2.2, 3.2)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E6Target6_shouldAssertEqual(self):
        eSeries = model.E_6
        targetValue = 6.28
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 4.7, 6.2)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E12Target8_shouldAssertEqual(self):
        eSeries = model.E_12
        targetValue = 8.3
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 6.8, 8.3)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E24Target9_shouldAssertEqual(self):
        eSeries = model.E_24
        targetValue = 9
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 7.5, 9.0)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E48Target6_shouldAssertEqual(self):
        eSeries = model.E_48
        targetValue = 6.28
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.15, 5.11, 6.3)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E96Target2_shouldAssertEqual(self):
        eSeries = model.E_96
        targetValue = 2.465
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 1.47, 2.5)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E192Target3_shouldAssertEqual(self):
        eSeries = model.E_192
        targetValue = 3.14
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 2.08, 3.1)
        self.assertEqual(modelOutput, PassiveComp.calculateSeries(eSeries, targetValue))

    def test_emptyList_shouldThrow(self):
        with self.assertRaises(ValueError):
            PassiveComp.calculateSeries([], 3.14)

    def test_underMinValue_shouldThrow(self):
        with self.assertRaises(ValueError):
            PassiveComp.calculateSeries(
                model.E_3, (model.E_3[0] * 2) - 1.1
            )  # or just 0 as min value?

    def test_overMaxValue_shouldThrow(self):
        with self.assertRaises(ValueError):
            PassiveComp.calculateSeries(model.E_3, (model.E_3[-1] * 2) + 1.1)
