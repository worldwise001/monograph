
import React, { Component } from 'react';
import {Button, Container, Form} from "react-bootstrap";

class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: []
        };
    }

    componentDidMount() {
        fetch("/api/library")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        items: result.items
                    });
                },
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    getCheckBoxes(items) {
        let checkboxes = [];
        for (let i = 0; i < items.length; i++) {
            checkboxes.push(<Form.Check type="checkbox" label={items[i]['name']}
                                        key={items[i]['id']} id={items[i]['id']} />)
        }
        return checkboxes;
    }

    render() {
        return (
            <Container className={"container-content"}>
                <Form>
                    <Form.Group controlId="formQuery">
                        <Form.Label>Query</Form.Label>
                        <Form.Control type="query" placeholder="A cool paper title" />
                    </Form.Group>
                    <Form.Group controlId="formMembers">
                        {this.getCheckBoxes(this.state.items)}
                    </Form.Group>
                    <Button variant="primary" type="submit">
                        Search
                    </Button>
                </Form>
            </Container>
        );
    }
}

export default Search;