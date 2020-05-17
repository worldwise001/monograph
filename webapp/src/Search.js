/* eslint react/prop-types: 0 */
import React, {Component} from 'react';
import {Button, Card, Col, Container, Form} from "react-bootstrap";
import {withRouter} from "react-router-dom";
import Spinner from "./Spinner";

class Search extends Component {
    constructor(props) {
        super(props);
        const params = new URLSearchParams(this.props.location.search)
        let q = params.get('q');
        if (!q) {
            q = '';
        }
        let sort = params.get('sort');
        if (!sort) {
            sort = 'Score';
        }
        let limit = params.get('limit');
        if (!limit) {
            limit = '10';
        }
        this.state = {
            error: null,
            isLoaded: true,
            libraries: [],
            works: [],
            crossref: {
                count: 0,
                url: null,
            },
            query: {
                'q': q,
                'sort': sort,
                'limit': limit,
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
                    state.works = result.items;
                    state.crossref.count = result.total;
                    state.crossref.url = result.url;
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
        }
        fetch("/api/library")
            .then(res => res.json())
            .then(
                (result) => {
                    state.libraries = result.items;
                    this.setState(state);
                },
                (error) => {
                    state.error = error;
                    this.setState(state);
                }
            )
    }

    getCheckBoxes(items) {
        let checkboxes = [];
        for (let i = 0; i < items.length; i++) {
            checkboxes.push(<Form.Check type="checkbox" label={items[i]['name']}
                                        key={items[i]['id']} id={items[i]['id']}/>)
        }
        return checkboxes;
    }

    searchForm(items) {
        return (
            <Form onSubmit={this.handleSubmit}>
                <Form.Row>
                    <Form.Group as={Col} controlId="formQuery">
                        <Form.Label>Query</Form.Label>
                        <Form.Control type="text" placeholder="A cool paper title" name="q"
                                      onChange={this.handleInputChange} defaultValue={this.state.query.q}/>
                    </Form.Group>
                </Form.Row>

                <Form.Row>
                    <Form.Group as={Col} md="6" controlId="formMembers">
                        <Form.Label>Sources</Form.Label>
                        {this.getCheckBoxes(items)}
                    </Form.Group>
                    <Form.Group as={Col} md="2" controlId="formSort">
                        <Form.Label>Sort by</Form.Label>
                        <Form.Control as="select" defaultValue={this.state.query.sort} name="sort"
                                      onChange={this.handleInputChange}>
                            <option>Score</option>
                            <option>Published</option>
                            <option>Citations</option>
                        </Form.Control>
                    </Form.Group>
                    <Form.Group as={Col} md="2" controlId="formLimit">
                        <Form.Label>Number of results</Form.Label>
                        <Form.Control as="select" defaultValue={this.state.query.limit} name="limit"
                                      onChange={this.handleInputChange}>
                            <option>10</option>
                            <option>20</option>
                            <option>50</option>
                            <option>100</option>
                        </Form.Control>
                    </Form.Group>
                </Form.Row>
                <Form.Row>
                    <Form.Group>
                        <Button variant="primary" type="submit">
                            Search
                        </Button>
                    </Form.Group>
                </Form.Row>
            </Form>
        );
    }

    createCard(item) {
        let cardLink = '';
        if (item.pdf) {
            cardLink = <Card.Link href={item.pdf}>PDF</Card.Link>;
        }
        return (
            <Card key={item.doi} className='search-result'>
                <Card.Body>
                    <Card.Title>{item.title}</Card.Title>
                    <Card.Subtitle className="mb-2 text-muted">
                        {item.authors.map(author => `${author.given} ${author.family}`).join(', ')}
                    </Card.Subtitle>
                    <Card.Text>
                        DOI: {item.doi}<br/>
                        Year: {item.year}
                    </Card.Text>
                    {cardLink}
                </Card.Body>
            </Card>
        )
    }

    createCards(items) {
        let cards = [];
        for (let i = 0; i < items.length; i++) {
            cards.push(this.createCard(items[i]));
        }
        return cards;
    }

    render() {
        return (
            <Container className={"container-content"}>
                {this.searchForm(this.state.libraries)}
                <div className="search-results">
                    {!this.state.isLoaded && <Spinner/>}
                    {this.state.isLoaded && this.state.works.length > 0 && this.createCards(this.state.works)}
                </div>
            </Container>
        )
    }
}

export default withRouter(Search);