import React, { Component } from 'react';
import ReactTable from 'react-table';
import 'react-table/react-table.css'

class ProcessList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      processes: []
    };
    this.refreshProcessList();
    window.setInterval(this.refreshProcessList, 1000);
  }

  refreshProcessList = () => {
    // Get a new process list from the server
    fetch(`/processes`)
    .then(result => result.json())
    .then(processes => this.setState(processes))
  }

  render() {
    const columns = [
      {
        "Header": "PID",
        "accessor": "pid"
      },
      {
        "Header": "Name",
        "accessor": "name"
      },
      {
        "Header": "CPU%",
        "accessor": "cpu_percent"
      },
      {
        "Header": "RAM%",
        "accessor": "memory_percent"
      },
    ];
    return (
      <ReactTable columns={columns} data={this.state.processes} />
    );
  }
}

export default ProcessList;
