# RestAPI-Order
This REST API allows users to make an order from the given set of items and displays the order on the basis the given rules. The application creates a webpage with the menu shown on the top and a text box to submit the order. After submitting the menu the system displays the items ordered and if the order breaks any of the given rule the error is shown and user can again test their order.

Dependencies:
1. Python3
2. Pip
4. Flask
5. HTML
6. IDE (Pycharm)

Rules:
1. An order consists of a meal and collection of comma separated item Ids.
2. The system should return the name of the items ordered
3. The system should always return items in the following order: meal, side, drink
4. If multiple items are ordered, the number of items should be indicated
5. Each order must contain a main and a side
6. If no drink is ordered, water should be returned
7. At breakfast, multiple cups of coffee can be ordered
8. At lunch, multiple sides can be ordered
9. At dinner,dessert must be ordered
10. At dinner, water is always provided
