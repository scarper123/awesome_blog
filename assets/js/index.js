/**
 * Created by eghklmi on 8/24/2017.
 */

let React = require('react');
let ReactDOM = require('react-dom');


let PostList = React.createClass(
    {
        loadPostsFromServer: function () {
            $.ajax({
                url: this.props.url,
                datatype: 'json',
                cache: false,
                success: function (data) {
                    this.setState({data: data})
                }.bind(this)
            })
        },
        getInitialState: function () {
            return {data: []}
        },
        componentWillMount: function () {
            this.loadPostsFromServer();
            setInterval(this.loadPostsFromServer,
                this.props.pollInterval)
        },
        render: function () {
            let postNodes = null;
            if (this.state.data) {
                console.log("DATA!");
                postNodes = this.state.data.map(function (post) {
                    return <tr>
                        <td>{post.title}</td>
                        <td>{post.category.name}</td>
                        <td>{post.tags.reduce(function (tag1, tag2) {
                            return tag1.name + "|" + tag2.name
                        })}</td>
                        <td>{post.author.username}</td>
                        <td>{post.pub_date}</td>
                    </tr>
                })
            }
            return (
                <div>
                    <h1>Hello React!</h1>
                    <table>
                        <tr>
                            <th>Title</th>
                            <th>Category</th>
                            <th>Tags</th>
                            <th>Author</th>
                            <th>Pub Date</th>
                        </tr>
                        {postNodes}
                    </table>
                </div>
            )
        }
    }
);

ReactDOM.render(<PostList url="/blog/post/api/" pollInterval={1000 * 5}/>,
    document.getElementById('post_list'));