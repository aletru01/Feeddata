// SPDX-License-Identifier: MIT
pragma solidity >=0.4.21 <0.8.0;

import "./Oracle.sol";

contract OracleConscensus {
    int256 ValueOracle1;
    int256 ValueOracle2;
    int256 Value;
    uint256 LastCheckedDate;
    event valueChanged(int256 newValueFinal, int256 newValue1, int256 newValue2, uint256 newDate);
    function getOraclesData() public {
        bytes32 oracleId1 = 0xf0f370ad33d1e3e8e2d8df7197c40f62b5bc403553b103858359687491234491;
        bytes32 oracleId2 = 0xf0f370ad33d1e3e8e2d8df7197c40f62b5bc403553b103858359687491234491;
        address oracleAddress = 0x8ecEDdd1377E52d23A46E2bd3dF0aFE35B526D5F;
        Oracle oracleContract1 = Oracle(oracleAddress);
        Oracle oracleContract2 = Oracle(oracleAddress);
        (int256 value1, uint256 date1) = oracleContract1.getInt(oracleId1);
        (int256 value2, uint256 date2) = oracleContract2.getInt(oracleId2);
        ValueOracle1 = value1;
        ValueOracle2 = value2;
        LastCheckedDate = date1;
        int256 valueFinal = (value1 + value2)/2;
        emit valueChanged(valueFinal, value1, value2, date1);
    }
    function get() public view returns (int256, uint256) {
        return (Value, LastCheckedDate);
    }
}
