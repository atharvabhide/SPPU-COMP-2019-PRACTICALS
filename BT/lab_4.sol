// SPDX-License-Identifier: Bhide License
pragma solidity ^0.8.0;

contract StudentRegistry {
    struct Student {
        string name;
        uint256 age;
    }

    address private owner;
    Student[] private students;

    // Define an event to log the received Ether value
    event ReceivedEther(address indexed sender, uint256 value);

    constructor() {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    receive() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }

    fallback() external payable {
        emit ReceivedEther(msg.sender, msg.value);
    }

    function withdrawEther(uint256 amount) public onlyOwner {
        require(amount <= address(this).balance, "Insufficient contract balance");
        (bool sent, ) = payable(owner).call{value: amount}("");
        require(sent, "Failed to send Ether");
    }

    function addStudent(string memory name, uint256 age) public {
        students.push(Student(name, age));
    }

    function getStudent(uint256 index) public view returns (string memory, uint256) {
        require(index < students.length, "Student not found");
        return (students[index].name, students[index].age);
    }

    function getStudentCount() public view returns (uint256) {
        return students.length;
    }
}
