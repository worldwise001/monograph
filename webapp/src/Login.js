/* eslint react/prop-types: 0 */
import React, {Component} from 'react';
import {Button, Card, Col, Container, Form} from "react-bootstrap";

class Login extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username:'',
            password:''
        }
    }
    render() {
        return (
            <Container classname={"container-content"}>
                <Form>
                    <Form.Group controlId="formUsername">
                        <Form.Label>User Name</Form.Label>
                        <Form.Control type="username" placeholder="User Name"></Form.Control>
                    </Form.Group>

                    <Form.Group controlId="formPassword">
                        <Form.Label>Password</Form.Label>
                        <Form.Control type="password" placeholder=""></Form.Control>
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