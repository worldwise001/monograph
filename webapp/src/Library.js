import React, {Component} from 'react';
import {Card, CardDeck, Col, Container, Row} from "react-bootstrap";

class Library extends Component {
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

    createCard(member) {
        return (
            <Card key={member['id']}>
                <Card.Body>
                    <Card.Title>{member['id']} - {member['name']}</Card.Title>
                    <Card.Text>
                        Prefixes: {member['doi_prefixes'].join(', ')}<br />
                        Available Works: {member['available_works']}
                    </Card.Text>
                </Card.Body>
                <Card.Footer>
                    <small className="text-muted">Last updated {member['last_updated_human_readable']} ago</small>
                </Card.Footer>
            </Card>
        )
    }

    createRows(items) {
        let rows = [];
        for (let row_id = 0; row_id < Math.ceil(items.length / 3); row_id++) {
            let cards = [];
            for (let card_id = row_id*3; card_id < Math.min((row_id+1)*3, items.length); card_id++) {
                cards.push(this.createCard(items[card_id]))
            }
            rows.push(<Row key={row_id}><Col><CardDeck>{cards}</CardDeck></Col></Row>)
        }
        return rows;
    }

    render() {
        return (
            <div>
                <Container>
                    {this.createRows(this.state.items)}
                </Container>

            </div>
        );
    }
}

export default Library;