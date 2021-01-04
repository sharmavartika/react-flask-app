import React, {useEffect, useState} from 'react'
import {Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper} from '@material-ui/core';
import axios from 'axios';

const App = () => {
  const [employees, setEmployees] = useState({});
  useEffect(() => {
    getEmployees()
  },[])
  
  const getEmployees = async () => {
  const res = await axios.get('/employees');
  setEmployees(res.data)
  }
  return (
    <div className="App">
      <h1>Employees</h1>
      <TableContainer component={Paper}>
      <Table aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Id</TableCell>
            <TableCell >Name</TableCell>
            <TableCell >Email</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {employees.length > 0 ? employees.map((employee) => (
            <TableRow key={employee.id}>
              <TableCell component="th" scope="row">
                {employee.id}
              </TableCell>
              <TableCell >{employee.name}</TableCell>
              <TableCell >{employee.email}</TableCell>
            </TableRow>
          )): ''}
        </TableBody>
      </Table>
    </TableContainer>
    </div>
  );
}

export default App;
