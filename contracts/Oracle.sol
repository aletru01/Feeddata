// SPDX-License-Identifier: MIT
pragma solidity >=0.4.21 <0.8.0;

abstract contract Oracle {
    function getInt(bytes32) public view virtual returns (int256, uint256);
    }
