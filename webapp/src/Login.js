/* eslint react/prop-types: 0 */
import React, {Component} from 'react';
import {Button, Container, Form} from "react-bootstrap";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username:'',
            password:''
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleUserChange = this.handleUserChange.bind(this);
        this.handlePassChange = this.handlePassChange.bind(this);
    }
    handleChange(event) {
        const target = event.target;
        const name = target.name;
        let state = this.state;
        state.query[name] = target.value
    }
    handleUserChange(event) {
        this.setState({ username: event.target.value})
    }
    handlePassChange(event) {
        this.setState({ password: event.target.value})
    }
    handleSubmit(event) {
       
    }
    render() {
        return (
            <Container classname={"container-content"}>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group controlId="formUsername">
                        <Form.Label>User Name</Form.Label>
                        <Form.Control type="username" placeholder="User Name" 
                                      name="username" onChange={this.handleUserChange}></Form.Control>
                    </Form.Group>

                    <Form.Group controlId="formPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="" name="password" 
                                      onChange={this.handlePassChange}></Form.Control>
                    </Form.Group>  
                    <Button variant="primary" type="submit">
                        Submit
                    </Button>                 
                </Form>
            </Container>
        )
    }
}

export default Login