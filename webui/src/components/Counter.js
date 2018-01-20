import React, { Component } from 'react';

class Counter extends Component {
  constructor(props) {
    super(props);
    this.state = {
       counter: 27
    };
    window.setInterval(this.upCounter, 1000);
  }

  upCounter = () => {
    this.setState({ counter: (this.state.counter + 1) });
  }

  render() {
    return (
      <span>
        {this.state.counter}
      </span>
    );
  }
}

export default Counter;
