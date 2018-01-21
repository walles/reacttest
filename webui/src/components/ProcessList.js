import React, { Component } from 'react';

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
    return (
      <ul>
        {this.state.processes.map(process => <li key={process}>{process}</li>)}
      </ul>
    );
  }
}

export default ProcessList;
