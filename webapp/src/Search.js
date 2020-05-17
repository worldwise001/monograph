/* eslint react/prop-types: 0 */
import React, {Component} from 'react';
import {Button, Card, Col, Container, Form} from "react-bootstrap";
import {withRouter} from "react-router-dom";
import Spinner from "./Spinner";

class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            items: [],
            query: {
                'q': '',
                'sort': 'Score',
                'limit': '10',
            }
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
    }

    handleInputChange(event) {
        const target = event.target;
        const name = target.name;
        let state = this.state;
        state.query[name] = target.value;
        this.setState(state);
    }

    handleSubmit(event) {
        event.preventDefault();
        const queryString = '?' + new URLSearchParams(this.state.query).toString();
        this.props.history.push({
            pathname: '/search',
            search: queryString
        });
        this.searchFetch(queryString);
    }

    searchFetch(queryString) {
        let state = this.state;
        state.isLoaded = false;
        this.setState(state);
        fetch("/api/search" + queryString)
            .then(res => res.json())
            .then(
                (result) => {
                    state.isLoaded = true;
                    state.items = [];
                    this.setState(state);
                },
                (error) => {
                    state.isLoaded = true;
                    state.error = error;
                    this.setState(state);
                }
            )
    }

    componentDidMount() {
        let state = this.state;
        if (this.props.location.search) {
            this.searchFetch(this.props.location.search);
        } else {
            fetch("/api/library")
                .then(res => res.json())
                .then(
                    (result) => {
                        state.isLoaded = true;
                        state.items = result.items;
                        this.setState(state);
                    },
                    (error) => {
                        state.isLoaded = true;
                        state.error = error;
                        this.setState(state);
                    }
                )
        }
    }

    getCheckBoxes(items) {
        let checkboxes = [];
        for (let i = 0; i < items.length; i++) {
            checkboxes.push(<Form.Check type="checkbox" label={items[i]['name']}
                                        key={items[i]['id']} id={items[i]['id']}/>)
        }
        return checkboxes;
    }

    renderSearchQuery(items) {
        return (
            <Container className={"container-content"}>
                <Form onSubmit={this.handleSubmit}>
                    <Form.Row>
                        <Form.Group as={Col} controlId="formQuery">
                            <Form.Label>Query</Form.Label>
                            <Form.Control type="text" placeholder="A cool paper title" name="q"
                                          onChange={this.handleInputChange}/>
                        </Form.Group>
                    </Form.Row>

                    <Form.Row>
                        <Form.Group as={Col} md="6" controlId="formMembers">
                            <Form.Label>Sources</Form.Label>
                            {this.getCheckBoxes(items)}
                        </Form.Group>
                        <Form.Group as={Col} md="2" controlId="formSort">
                            <Form.Label>Sort by</Form.Label>
                            <Form.Control as="select" defaultValue="Score" name="sort"
                                          onChange={this.handleInputChange}>
                                <option>Score</option>
                                <option>Published</option>
                                <option>Citations</option>
                            </Form.Control>
                        </Form.Group>
                        <Form.Group as={Col} md="2" controlId="formLimit">
                            <Form.Label>Number of results</Form.Label>
                            <Form.Control as="select" defaultValue="10" name="limit"
                                          onChange={this.handleInputChange}>
                                <option>10</option>
                                <option>20</option>
                                <option>50</option>
                                <option>100</option>
                            </Form.Control>
                        </Form.Group>
                    </Form.Row>
                    <Form.Row>
                        <Button variant="primary" type="submit">
                            Search
                        </Button>
                    </Form.Row>
                </Form>
            </Container>
        );
    }

    renderCard(i, item) {
        return (
            <Card className='search-result'>
                <Card.Body>
                    <Card.Title>Card Title</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
                    <Card.Text>
                        Some quick example text to build on the card title and make up the bulk of
                        the card content.
                    </Card.Text>
                    <Card.Link href="#">Card Link</Card.Link>
                    <Card.Link href="#">Another Link</Card.Link>
                </Card.Body>
            </Card>
        )
    }

    renderCards(items) {
        return (
            <div>
                <Card>
                    <Card.Body>
                        <Card.Title>Card Title</Card.Title>
                        <Card.Subtitle className="mb-2 text-muted">Card Subtitle</Card.Subtitle>
                        <Card.Text>
                            Some quick example text to build on the card title and make up the bulk of
                            the card content.
                        </Card.Text>
                        <Card.Link href="#">Card Link</Card.Link>
                        <Card.Link href="#">Another Link</Card.Link>
                    </Card.Body>
                </Card>
            </div>
        )
    }

    renderSearchResults(items) {
        return (
            <Container className={"container-content"}>
                {!this.state.isLoaded && <Spinner/>}
                {this.state.isLoaded && this.renderCards(items)}
            </Container>
        );
    }

    render() {
        if (this.props.location.search) {
            return this.renderSearchResults(this.state.items);
        } else {
            return this.renderSearchQuery(this.state.items);
        }
    }
}

export default withRouter(Search);