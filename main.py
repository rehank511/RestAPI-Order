from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST'])
def home():

    b1 = "Eggs"
    b2 = "Toast"
    b3 = "Coffee"
    l1 = "Salad"
    l2 = "Chips"
    l3 = "Soda"
    d1 = "Steak"
    d2 = "Potatoes"
    d3 = "Wine"
    d4 = "Cake"
    water = "Water"
    message = []
    errormsg = ['Unable to Process: ']

    if request.method == 'POST':
        order = request.form.get('Order')
        order = order.replace(",", " ")
        order = order.split(" ")
        meal = order.pop(0)
        count1 = 0
        count2 = 0
        count3 = 0
        count4 = 0
        error = 0

        if meal == 'Breakfast' or meal == 'breakfast':
            for x in order:
                if x == "1":
                    count1 += 1
                if x == "2":
                    count2 += 1
                if x == "3":
                    count3 += 1

            if count1 < 1:
                errormsg.append("Main is Missing")
                error = 1
            elif count1 > 1:
                errormsg.append("Only one serving of " + b1 + " can be ordered")
                error = 1
            else:
                message.append(b1)

            if count2 < 1:
                errormsg.append("Side is Missing")
                error = 1
            elif count2 > 1:
                errormsg.append("Only one serving of " + b2 + " can be ordered")
                error = 1
            else:
                message.append(b2)

            if count3 < 1:
                message.append(water)
            else:
                if count3 == 1:
                    message.append(b3)
                else:
                    message.append(b3 + "-" + str(count3))

            if error == 0:
                return "<a href=\"http://localhost:5000/\">HOME</a> <p> {} </p>".format(message)
            else:
                return "<a href=\"http://localhost:5000/\">HOME</a> <p> {} </p>".format(errormsg)

        elif meal == 'Lunch' or meal == 'lunch':
            for x in order:
                if x == "1":
                    count1 += 1
                if x == "2":
                    count2 += 1
                if x == "3":
                    count3 += 1

            if count1 < 1:
                errormsg.append("Main is Missing")
                error = 1
            elif count1 > 1:
                errormsg.append("Only one serving of " + l1 + " can be ordered")
                error = 1
            else:
                message.append(l1)

            if count2 < 1:
                errormsg.append("Side is Missing")
                error = 1
            else:
                if count2 == 1:
                    message.append(l2)
                else:
                    message.append(l2 + "-" + str(count2))

            if count3 < 1:
                message.append(water)
            else:
                if count3 == 1:
                    message.append(l3)
                else:
                    message.append(l3 + "-" + str(count3))

            if error == 0:
                return "<a href=\"http://localhost:5000/\">HOME</a> <p> {} </p>".format(message)
            else:
                return "<a href=\"http://localhost:5000/\">HOME</a> <p> {} </p>".format(errormsg)

        elif meal == 'Dinner' or meal == 'dinner':
            for x in order:
                if x == "1":
                    count1 += 1
                if x == "2":
                    count2 += 1
                if x == "3":
                    count3 += 1
                if x == "4":
                    count4 += 1

            if count1 < 1:
                errormsg.append("Main is Missing")
                error = 1
            elif count1 > 1:
                errormsg.append("Only one serving of " + d1 + " can be ordered")
                error = 1
            else:
                message.append(d1)

            if count2 < 1:
                errormsg.append("Side is Missing")
                error = 1
            else:
                if count2 == 1:
                    message.append(d2)
                else:
                    message.append(d2 + "-" + str(count2))

            if count3 >= 1:
                if count3 == 1:
                    message.append(d3)
                else:
                    message.append(d3 + "-" + str(count3))

            message.append(water)

            if count4 < 1:
                errormsg.append("Dessert is Missing")
                error = 1
            elif count4 > 1:
                errormsg.append("Only one serving of " + d4 + " can be ordered")
                error = 1
            else:
                message.append(d4)

            if error == 0:
                return "<a href=\"http://localhost:5000/\">HOME</a> <p> {} </p>".format(message)
            else:
                return "<a href=\"http://localhost:5000/\">HOME</a> <p> {} </p>".format(errormsg)

        else:
            return "<a href=\"http://localhost:5000/\">HOME</a> <p> The meal preference is not mentioned correctly </p>"

    return "<html>" \
           "<head>" \
           "<style>" \
           "table, th, td {" \
           "border: 1px solid black;" \
           "border-collapse: collapse;" \
           "}" \
           "table {" \
           "width: 50%;" \
           "height: 50;" \
           "}" \
           "</style>" \
           "<title> Order Here! </title>" \
           "</head>" \
           "<p> <u> Breakfast </u> </p>" \
           "<table>" \
           "<tr>" \
           "<th>Main</th>" \
           "<th>Side</th>" \
           "<th>Drink</th>" \
           "</tr>" \
           "<tr>" \
           "<td>1. Eggs</td>" \
           "<td>2. Toast</td>" \
           "<td>3. Coffee</td>" \
           "</tr>" \
           "</table>" \
           "<p> <u> Lunch </u> </p>" \
           "<table>" \
           "<tr>" \
           "<th>Main</th>" \
           "<th>Side</th>" \
           "<th>Drink</th>" \
           "</tr>" \
           "<tr>" \
           "<td>1. Salad</td>" \
           "<td>2. Chips</td>" \
           "<td>3. Soda</td>" \
           "</tr>" \
           "</table>" \
           "<p> <u> Dinner </u> </p>" \
           "<table>" \
           "<tr>" \
           "<th>Main</th>" \
           "<th>Side</th>" \
           "<th>Drink</th>" \
           "<th>Desert</th>" \
           "</tr>" \
           "<tr>" \
           "<td>1. Steak</td>" \
           "<td>2. Potatoes</td>" \
           "<td>3. Wine</td>" \
           "<td>4. Cake</td>" \
           "</tr>" \
           "</table>" \
           "<br>" \
           "<form method = \"POST\">" \
           "<p>Order <input type = \"text\" name = \"Order\" /></p>" \
           "<p><input type = \"submit\" value = \"submit\" /></p>" \
           "</form>" \
           "</html>"


app.run(port=5000)
