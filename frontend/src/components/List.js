import React, { useEffect, useState } from "react";
import axios from "axios";
const List = () => {
  const [todos, setTodos] = useState([]);
  const getTodos = async () => {
    const res = await axios.get("http://localhost:8000/api/todos");
    console.log(res);
    setTodos(res.data);
  };
  useEffect(() => {
    getTodos();
  }, []);
  return (
    <div className="container">
      {todos.length > 0 &&
        todos.map((todo) => (
          <div
            className="card"
            key={todo.id}
            style={{ width: "428px", padding: "20px 10px" }}
          >
            <div className="card-title d-flex align-items-center justify-content-between">
              <h2>{todo.title}</h2>
              <input type="checkbox" defaultChecked={todo.completed} />
            </div>
            <div className="card-body">
              <p>{todo.description}</p>
            </div>
            <div className="card-footer">
              <span>Created at: {todo.created_at}</span>
            </div>
          </div>
        ))}
    </div>
  );
};
export default List;
