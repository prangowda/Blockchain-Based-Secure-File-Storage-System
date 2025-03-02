// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FileStorage {
    struct File {
        string hash;
        string fileName;
        uint256 timestamp;
    }

    mapping(string => File) private files;
    event FileStored(string hash, string fileName, uint256 timestamp);

    function storeFile(string memory _hash, string memory _fileName) public {
        require(bytes(files[_hash].hash).length == 0, "File already exists");
        files[_hash] = File(_hash, _fileName, block.timestamp);
        emit FileStored(_hash, _fileName, block.timestamp);
    }

    function verifyFile(string memory _hash) public view returns (string memory, uint256) {
        require(bytes(files[_hash].hash).length > 0, "File not found");
        return (files[_hash].fileName, files[_hash].timestamp);
    }
}
