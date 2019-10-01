import pytest
import sys
from circuits import (LogicGate, BinaryGate, AndGate, OrGate, NandGate, NorGate, XorGate,
                    UnaryGate, NotGate, Connector)

def make_multiple_inputs(inputs):
    """ provides a function to call for every input requested. """
    def next_input(_):
        """ provides the first item in the list. """
        return inputs.pop()
    return next_input


# Tests for LogicGate Class
@pytest.fixture
def logic_gate():
    return LogicGate('LG')

@pytest.mark.LogicGate
def test_LogicGate_constructor(logic_gate):
    ''' Test that class constructor works'''
    testGate = logic_gate
    assert testGate.name == 'LG'
    assert testGate.output == None

@pytest.mark.LogicGate
def test_LogicGate_constructor_noinput():
    '''Test that class raises TypeError for missing data'''
    with pytest.raises(TypeError):
        testGate = LogicGate()

@pytest.mark.LogicGate
def test_LogicGate_getLabel(logic_gate):
    '''Test getLabel Method of LogicGate class'''
    assert logic_gate.getLabel() == 'LG'


# Tests for BinaryGate Class
@pytest.fixture
def binary_gate():
    return BinaryGate('BG')

@pytest.mark.BinaryGate
def test_BinaryGate_constuctor(binary_gate):
    '''Test that class constructor works'''
    assert binary_gate.name == 'BG'
    assert binary_gate.output == None

@pytest.mark.BinaryGate
def test_BinaryGate_getPinA(binary_gate, monkeypatch):
    '''Test getPinA methods of BinaryGate class'''
    # Use monkeypatch to modify input fuctino and pass in value
    monkeypatch.setattr('builtins.input', lambda x: 1)
    assert binary_gate.getPinA() == 1

@pytest.mark.BinaryGate
def test_BinaryGate_getPinB(binary_gate, monkeypatch):
    '''Test getPinB methods of BinaryGate class'''
    # Use monkeypatch to modify input function and pass in value
    monkeypatch.setattr('builtins.input', lambda x: 1)
    assert binary_gate.getPinB() == 1

@pytest.mark.BinaryGate
def test_BinaryGate_setNextPin(binary_gate, capsys):
    '''test setNextPin() Method of BinaryGate class'''
    assert binary_gate.pinA == None
    assert binary_gate.pinB == None
    
    binary_gate.setNextPin(1)
    assert binary_gate.pinA == 1
    assert binary_gate.pinB == None
    
    binary_gate.setNextPin(0)
    assert binary_gate.pinA == 1
    assert binary_gate.pinB == 0
    
    binary_gate.setNextPin(0)
    # Use capsys to captue the system output to make sure the desired message is displayed
    assert capsys.readouterr().out == "Cannot Connect: NO EMPTY PINS on this gate\n"


# Test for AndGate Class
@pytest.fixture
def and_gate():
    return AndGate('AG')

@pytest.mark.AndGate
def test_AndGate_Constructor(and_gate):
    '''Test that class constructor works'''
    assert and_gate.name == 'AG'
    assert and_gate.output == None
    assert and_gate.pinA == None
    assert and_gate.pinB == None

@pytest.mark.parametrize('pinA, pinB, output',
                        [(0, 0, 0),
                         (0, 1, 0),
                         (1, 0, 0),
                         (1, 1, 1)])
@pytest.mark.AndGate
def test_AndGate_performGateLogic(pinA, pinB, output, and_gate, monkeypatch):
    '''Test performGateLogic method of AndGate class'''
    # Use monkeypatch to modify input function and pass in value
    # make_multiple_inputs pops and item from the paramatrized list for every input call
    monkeypatch.setattr('builtins.input', make_multiple_inputs([pinB, pinA]))
    assert and_gate.performGateLogic() == output
    

# Test for NandGate Class
@pytest.fixture
def nand_gate():
    return NandGate('NandG')

@pytest.mark.NandGate
def test_NandGate_Constructor(nand_gate):
    '''Test that class constructor works'''
    assert nand_gate.name == 'NandG'
    assert nand_gate.output == None
    assert nand_gate.pinA == None
    assert nand_gate.pinB == None

@pytest.mark.parametrize('pinA, pinB, output',
                        [(0, 0, 1),
                         (0, 1, 1),
                         (1, 0, 1),
                         (1, 1, 0)])
@pytest.mark.NandGate
def test_NandGate_performGateLogic(pinA, pinB, output, nand_gate, monkeypatch):
    '''Test performGateLogic method of NandGate class'''
    # Use monkeypatch to modify input function and pass in value
    # make_multiple_inputs pops and item from the paramatrized list for every input call
    monkeypatch.setattr('builtins.input', make_multiple_inputs([pinB, pinA]))
    assert nand_gate.performGateLogic() == output


# Tests for OrGate
@pytest.fixture
def or_gate():
    return OrGate('OG')

@pytest.mark.OrGate
def test_OrGate_Constructor(or_gate):
    '''Test that class constructor works'''
    assert or_gate.name == 'OG'
    assert or_gate.output == None
    assert or_gate.pinA == None
    assert or_gate.pinB == None

@pytest.mark.parametrize('pinA, pinB, output',
                        [(0, 0, 0),
                         (0, 1, 1),
                         (1, 0, 1),
                         (1, 1, 1)])
@pytest.mark.OrGate
def test_OrGate_performGateLogic(pinA, pinB, output, or_gate, monkeypatch):
    '''Test performGateLogic method of OrGate class'''
    # Use monkeypatch to modify input function and pass in value
    # make_multiple_inputs pops and item from the paramatrized list for every input call
    monkeypatch.setattr('builtins.input', make_multiple_inputs([pinB, pinA]))
    assert or_gate.performGateLogic() == output


# Tests for NorGate
@pytest.fixture
def nor_gate():
    return NorGate('NorG')

@pytest.mark.NorGate
def test_NorGate_Constructor(nor_gate):
    '''Test that class constructor works'''
    assert nor_gate.name == 'NorG'
    assert nor_gate.output == None
    assert nor_gate.pinA == None
    assert nor_gate.pinB == None

@pytest.mark.parametrize('pinA, pinB, output',
                        [(0, 0, 1),
                         (0, 1, 0),
                         (1, 0, 0),
                         (1, 1, 0)])
@pytest.mark.NorGate
def test_NorGate_performGateLogic(pinA, pinB, output, nor_gate, monkeypatch):
    '''Test performGateLogic method of NorGate class'''
    # Use monkeypatch to modify input function and pass in value
    # make_multiple_inputs pops and item from the paramatrized list for every input call
    monkeypatch.setattr('builtins.input', make_multiple_inputs([pinB, pinA]))
    assert nor_gate.performGateLogic() == output


# Tests for XorGate
@pytest.fixture
def xor_gate():
    return XorGate('XG')

@pytest.mark.XorGate
def test_XorGate_Constructor(xor_gate):
    '''Test that class constructor works'''
    assert xor_gate.name == 'XG'
    assert xor_gate.output == None
    assert xor_gate.pinA == None
    assert xor_gate.pinB == None

@pytest.mark.parametrize('pinA, pinB, output',
                        [(0, 0, 0),
                         (0, 1, 1),
                         (1, 0, 1),
                         (1, 1, 0)])
@pytest.mark.XorGate
def test_XorGate_performGateLogic(pinA, pinB, output, xor_gate, monkeypatch):
    '''Test performGateLogic method of XorGate class'''
    # Use monkeypatch to modify input function and pass in value
    # make_multiple_inputs pops and item from the paramatrized list for every input call
    monkeypatch.setattr('builtins.input', make_multiple_inputs([pinB, pinA]))
    assert xor_gate.performGateLogic() == output


# Tests for UnaryGate
@pytest.fixture
def unary_gate():
    return UnaryGate('UG')

@pytest.mark.UnaryGate
def test_UnaryGate_Constructor(unary_gate):
    '''Test that class constructor works'''
    assert unary_gate.name == 'UG'
    assert unary_gate.pin == None
    assert unary_gate.output == None

@pytest.mark.UnaryGate
def test_UnaryGate_getPin(unary_gate, monkeypatch):
    '''Test getPin() method of UnaryGate class'''
    # Use monkeypatch to modify input function and pass in value
    monkeypatch.setattr('builtins.input', lambda x: 1)
    assert unary_gate.getPin() == 1


@pytest.mark.UnaryGate
def test_UnaryGate_setNextPin(unary_gate, capsys):
    '''test setNextPin() Method of BinaryGate class'''
    assert unary_gate.pin == None
    
    unary_gate.setNextPin(1)
    assert unary_gate.pin == 1

    unary_gate.setNextPin(0)
    # Use capsys to captue the system output to make sure the desired message is displayed
    assert capsys.readouterr().out == "Cannot Connect: NO EMPTY PINS on this gate\n"


# Tests for NotGate class
@pytest.fixture
def not_gate():
    return NotGate('NotG')

@pytest.mark.NotGate
def test_NotGate_Constructor(not_gate):
    ''' Test that class constructor works'''
    assert not_gate.name == 'NotG'
    assert not_gate.pin == None
    assert not_gate.output == None

@pytest.mark.parametrize('pin, output',
                        [(1, 0),
                         (0, 1)])
@pytest.mark.NotGate
def test_NotGate_performGateLogic(pin, output, not_gate, monkeypatch):
    ''' Test performGateLogic() method of NotGate class'''
    # Use monkeypatch to modify input function and pass in value
    monkeypatch.setattr('builtins.input', lambda x: pin)
    assert not_gate.performGateLogic() == output


# Tests for Connector class
@pytest.fixture()
def connector(and_gate, not_gate):
    # Set up gate --> eventually parametrize for exhaustive testing?
    return Connector(and_gate, not_gate)

@pytest.mark.Connector
def test_Connector_Constuctor(connector):
    '''Test that class constructor works'''
    assert connector.fromGate.getLabel() == 'AG'
    assert connector.toGate.getLabel() == 'NotG'

# Tests for system functionality
@pytest.mark.parametrize ('G1Pa, G1Pb, G2Pa, G2Pb, output',
                        [(0, 1, 1, 1, 0)])
@pytest.mark.Circuits
def test_circuit(G1Pa, G1Pb, G2Pa, G2Pb, output, monkeypatch):
    g1 = AndGate('G1')
    g2 = AndGate('G2')
    g3 = OrGate('G3')
    g4 = NotGate('G4')

    c1 = Connector(g1, g3)
    c2 = Connector(g2, g3)
    c3 = Connector(g3,g4)

    monkeypatch.setattr('builtins.input', make_multiple_inputs(G2Pb, G2Pa, G1Pb, G1Pa))
    assert g4.getOutput() == output


    