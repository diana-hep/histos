#!/usr/bin/env python

# Copyright (c) 2018, DIANA-HEP
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest

from histos import *

class Test(unittest.TestCase):
    def runTest(self):
        pass

    def test_Metadata(self):
        h = Collection("id", [], metadata=Metadata("""{"one": 1, "two": 2}""", language=Metadata.json))
        assert h.isvalid
        assert h.metadata.data == """{"one": 1, "two": 2}"""
        assert h.metadata.language == Metadata.json

    def test_Decoration(self):
        h = Collection("id", [], decoration=Decoration("""points { color: red }""", language=Decoration.css))
        assert h.isvalid
        assert h.decoration.data == """points { color: red }"""
        assert h.decoration.css == Decoration.css

    def test_RawInlineBuffer(self):
        pass

    def test_RawExternalBuffer(self):
        pass

    def test_InterpretedInlineBuffer(self):
        pass

    def test_InterpretedExternalBuffer(self):
        pass

    def test_Binning(self):
        pass

    def test_FractionalBinning(self):
        pass

    def test_IntegerBinning(self):
        pass

    def test_RealInterval(self):
        pass

    def test_RealOverflow(self):
        pass

    def test_RegularBinning(self):
        pass

    def test_TicTacToeOverflowBinning(self):
        pass

    def test_HexagonalBinning(self):
        pass

    def test_VariableBinning(self):
        pass

    def test_CategoryBinning(self):
        pass

    def test_SparseRegularBinning(self):
        pass

    def test_Axis(self):
        pass

    def test_Counts(self):
        pass

    def test_UnweightedCounts(self):
        pass

    def test_WeightedCounts(self):
        pass

    def test_Correlation(self):
        pass

    def test_Extremes(self):
        pass

    def test_Moments(self):
        pass

    def test_Quantiles(self):
        pass

    def test_GenericErrors(self):
        pass

    def test_DistributionStats(self):
        pass

    def test_Distribution(self):
        pass

    def test_Profile(self):
        pass

    def test_Histogram(self):
        pass

    def test_Parameter(self):
        h = Collection("id", [ParameterizedFunction("id", "x**2", [Parameter("x", 5), Parameter("y", 6)])])
        assert h.isvalid

    def test_ParameterizedFunction(self):
        h = Collection("id", [ParameterizedFunction("id", "x**2", [], contours=[1.1, 2.2, 3.3])])
        assert h.isvalid

    def test_EvaluatedFunction(self):
        pass

    # def test_BinnedEvaluatedFunction(self):
    #     h = Collection("id", [BinnedEvaluatedFunction("id", [], )])
    #     assert h.isvalid

    def test_Page(self):
        pass

    def test_ColumnChunk(self):
        pass

    def test_Chunk(self):
        pass

    def test_Column(self):
        pass

    def test_Ntuple(self):
        pass

    def test_Region(self):
        pass

    def test_BinnedRegion(self):
        pass

    def test_Assignment(self):
        pass

    def test_Variation(self):
        pass

    def test_collection(self):
        h = Collection("id", [])
        assert h.isvalid
        assert h.identifier == "id"
