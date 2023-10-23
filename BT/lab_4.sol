// SPDX-License-Identifier: Bhide License
pragma solidity ^0.8.0;

contract StudentRegistry {
    struct Student {
        string name;
        uint256 age;
    }

    Student[] private students;

    // Define an event to log the received Ether value
    event ReceivedEther(address indexed sender, uint256 value);

    receive() external payable {
        // This function can receive Ether, but it doesn't do anything in this example.
        // Log the received Ether value
        emit ReceivedEther(msg.sender, msg.value);
    }

    fallback() external payable {
        // Fallback function to receive Ether
        emit ReceivedEther(msg.sender, msg.value);
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