import React, { Component } from 'react';
import './ProcessList.css';

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
      <table>
      {this.state.processes.map(function(process){
        return (
          <tr key={process.pid} id={process.pid}>
            <td className="number">{process.pid}</td>
            <td className="number"><a href={"#"+process.ppid}>{process.ppid}</a></td>
            <td>{process.name}</td>
          </tr>
        );
      })}
      </table>
    );
  }
}

export default ProcessList;
