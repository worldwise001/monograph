/* eslint react/prop-types: 0 */
import React, {Component} from 'react';
import {Button, Container, Form} from "react-bootstrap";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "default",
            password: "default"
        };
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleInputChange(event) {
        const target = event.target;
        const name = target.name;
        this.setState({ [name]: target.value })
    }
    handleSubmit(event) {
        event.preventDefault();
        let state = this.state;
        state.isLoaded = false;

        fetch("/api/login", {
            method: 'POST',

            body: JSON.stringify({
                username: state.username,
                password: state.password
            })
        })
        .then(resp => {
            if (resp.ok) {
                return resp.json();
            } else {
                alert(":DD")
                throw new Error("test")
            }
        })
        .then(res => res.json())
        .then(result => alert(result.success))
        .catch(error => alert(error.error))
    }
    render() {
        return (
            <Container className={"container-content"}>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Group controlId="formUsername">
                        <Form.Label>User Name</Form.Label>
                        <Form.Control type="username" placeholder="User Name" 
                                      name="username" onChange={this.handleInputChange}></Form.Control>
                    </Form.Group>

                    <Form.Group controlId="formPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder="" name="password" 
                                      onChange={this.handleInputChange}></Form.Control>
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