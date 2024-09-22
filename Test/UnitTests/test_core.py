# to run tests python3 -m unittest Test.UnitTests.test_core from root dir
# python3 -m unittest Test.UnitTests.test_core 2>&1 | grep -A 10 ERROR

import unittest

import PassiveComp.core as passiveComp
import Test.Model.eseries as model


class TestCreateSeries(unittest.TestCase):
    def test_happyPathE3compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_3, passiveComp.createSeries(3))

    def test_happyPathE6compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_6, passiveComp.createSeries(6))

    def test_happyPathE12compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_12, passiveComp.createSeries(12))

    def test_happyPathE24compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_24, passiveComp.createSeries(24))

    def test_happyPathE48compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_48, passiveComp.createSeries(48))

    def test_happyPathE96compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_96, passiveComp.createSeries(96))

    def test_happyPathE192compareToModel_shouldAssertEqual(self):
        self.assertEqual(model.E_192, passiveComp.createSeries(192))

    def test_invalidParameter_negative_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(-6)

    def test_invalidParameter_0_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(0)

    def test_invalidParameter_float_shouldThrow(self):
        with self.assertRaises(TypeError):
            passiveComp.createSeries(3.3)

    def test_invalidParameter_2_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(2)

    def test_invalidParameter_4_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(4)

    def test_invalidParameter_5_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(5)

    def test_invalidParameter_7_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(7)

    def test_invalidParameter_11_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(11)

    def test_invalidParameter_13_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(13)

    def test_invalidParameter_23_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(23)

    def test_invalidParameter_25_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(25)

    def test_invalidParameter_47_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(47)

    def test_invalidParameter_49_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(49)

    def test_invalidParameter_95_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(95)

    def test_invalidParameter_97_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(97)

    def test_invalidParameter_191_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(191)

    def test_invalidParameter_193_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.createSeries(193)


class TestCalculateSeries(unittest.TestCase):
    def test_happyPathcompareToModel_E3Target3_shouldAssertEqual(self):
        eSeries = model.E_3
        targetValue = 3.14
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 2.2, 3.2)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E6Target6_shouldAssertEqual(self):
        eSeries = model.E_6
        targetValue = 6.28
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 4.7, 6.2)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E12Target8_shouldAssertEqual(self):
        eSeries = model.E_12
        targetValue = 8.3
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 6.8, 8.3)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E24Target9_shouldAssertEqual(self):
        eSeries = model.E_24
        targetValue = 9
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.5, 7.5, 9.0)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E48Target6_shouldAssertEqual(self):
        eSeries = model.E_48
        targetValue = 6.28
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.15, 5.11, 6.3)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E96Target2_shouldAssertEqual(self):
        eSeries = model.E_96
        targetValue = 2.465
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 1.47, 2.5)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_happyPathcompareToModel_E192Target3_shouldAssertEqual(self):
        eSeries = model.E_192
        targetValue = 3.14
        # modelOutput = Model.calculateSeries(eSeries,targetValue)
        modelOutput = (1.0, 2.08, 3.1)
        self.assertEqual(modelOutput, passiveComp.calculateSeries(eSeries, targetValue))

    def test_emptyList_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.calculateSeries([], 3.14)

    def test_underMinValue_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.calculateSeries(
                model.E_3, (model.E_3[0] * 2) - 1.1
            )  # or just 0 as min value?

    def test_overMaxValue_shouldThrow(self):
        with self.assertRaises(ValueError):
            passiveComp.calculateSeries(model.E_3, (model.E_3[-1] * 2) + 1.1)
