#######################################################
#   Author:     <Kaiwen Yu>
#   email:      <yu872@purdue.edu>
#   ID:         <ee364e08>
#   Date:       <10/4/2019>
#######################################################

import enum
import pprint


class Level(enum.Enum):
    Freshman = "Freshman"
    Sophomore = "Sophomore"
    Junior = "Junior"
    Senior = "Senior"


class ComponentType(enum.Enum):
    Resistor = "Resistor"
    Capacitor = "Capacitor"
    Inductor = "Inductor"
    Transistor = "Transistor"


class Student:

    def __init__(self, ID, firstName, lastName, level):
        self.ID = ID
        self.firstName = firstName
        self.lastName = lastName
        if level not in Level:
            raise TypeError("The argument must be an instance of the 'Level' Enum.")
        self.level = level

    def __str__(self):
        return f"{self.ID}, {self.firstName} {self.lastName}, {self.level.value}"


class Component:

    def __init__(self, ID, ctype: ComponentType, price):
        self.ID = ID
        self.price = price
        if ctype not in ComponentType:
            raise TypeError("The component type must be an instance of the 'ComponentType' Enum.")
        self.ctype = ctype

    def __str__(self):
        return f"{self.ctype.value}, {self.ID}, ${'%.2f' % self.price}"

    def __repr__(self):
        return f"<{self.ctype.value}, {self.ID}, ${'%.2f' % self.price}>"

    def __hash__(self):
        return hash(self.ID)


class Circuit:
    def __init__(self, ID: str, components: set):
        self.ID = ID
        price = 0.00
        if components:
            self.components = components
            for component in components:
                if component.ctype not in ComponentType:
                    raise TypeError("The components must be a set of Component class.")
                price += component.price
        self.cost = round(price, 2)

    def __str__(self):
        r = c = i = t = 0
        if self.components:
            for component in self.components:
                if component.ctype == ComponentType.Resistor:
                    r += 1
                elif component.ctype == ComponentType.Capacitor:
                    c += 1
                elif component.ctype == ComponentType.Inductor:
                    i += 1
                elif component.ctype == ComponentType.Transistor:
                    t += 1
        return f"{self.ID}: (R = {'%02d' % r}, C = {'%02d' % c}, I = {'%02d' % i}, T = {'%02d' % t}), Cost = ${'%.2f' % self.cost}"

    def getByType(self, type: ComponentType):
        final_set = set()
        if type not in ComponentType:
            raise ValueError("The type is a wrong type!")
        if self.components:
            for component in self.components:
                if component.ctype == type:
                    final_set.add(component)
        return final_set

    def __contains__(self, item: Component):
        if isinstance(item, Component):
            if item in self.components:
                return True
            else:
                return False
        else:
            raise TypeError("That item is not an instance of Component class!")

    def __add__(self, other: Component):
        if isinstance(other, Component):
            if other not in self.components:
                self.components.add(other)
                self.cost += other.price
            return self
        else:
            raise TypeError("The new item is not an instance of Component class!")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other: Component):
        if isinstance(other, Component):
            if other in self.components:
                self.components.discard(other)
                self.cost -= other.price
            return self
        else:
            raise TypeError("The new item is not an instance of Component class!")

    def __eq__(self, other):
        if isinstance(other, Circuit):
            if self.cost == other.cost:
                return True
            else:
                return False
        else:
            raise TypeError("The second item is not an instance of Circuit class!")

    def __lt__(self, other):
        if isinstance(other, Circuit):
            if self.cost < other.cost:
                return True
            else:
                return False
        else:
            raise TypeError("The second item is not an instance of Circuit class!")

    def __gt__(self, other):
        if isinstance(other, Circuit):
            if self.cost > other.cost:
                return True
            else:
                return False
        else:
            raise TypeError("The second item is not an instance of Circuit class!")


class Project:

    def __init__(self, ID: str, participants: list, circuits: list):
        self.ID = ID
        if participants:
            for par in participants:
                if not isinstance(par, Student):
                    raise TypeError("The participants list contains something not an instance of Student class!")
        if circuits:
            for cir in circuits:
                if not isinstance(cir, Circuit):
                    raise TypeError("The circuits list contains something not an instance of Circuit class!")
        self.participants = participants
        self.circuits = circuits
        price = 0.0
        for cir in circuits:
            price += cir.cost
        self.cost = round(price, 2)

    def __str__(self):
        c = len(self.circuits)
        p = len(self.participants)
        return f"{self.ID}: ({'%02d' % c} Circuits, {'%02d' % p} Participants), Cost = ${'%.2f' % self.cost}"

    def __contains__(self, item):
        if isinstance(item, Component):
            component_set = set()
            for cir in self.circuits:
                for comp in cir.components:
                    component_set.add(comp.ID)
            if item.ID in component_set:
                return True
            else:
                return False
        elif isinstance(item, Circuit):
            circuit_set = set()
            for cir in self.circuits:
                circuit_set.add(cir.ID)
            if item.ID in circuit_set:
                return True
            else:
                return False
        elif isinstance(item, Student):
            student_set = set()
            for student in self.participants:
                student_set.add(student.ID)
            if item.ID in student_set:
                return True
            else:
                return False
        else:
            raise TypeError("That item is not an instance of Component/Circuit/Student class!")

    def __add__(self, other: Circuit):
        if isinstance(other, Circuit):
            if other not in self.circuits:
                self.circuits.append(other)
                self.cost += other.cost
                round(self.cost, 2)
            return self
        else:
            raise TypeError("The new item is not an instance of Circuit class!")

    def __sub__(self, other: Circuit):
        if isinstance(other, Circuit):
            if other in self.circuits:
                self.circuits.remove(other)
                self.cost -= other.cost
                round(self.cost, 2)
            return self
        else:
            raise TypeError("The new item is not an instance of Circuit class!")

    def __getitem__(self, item: str):
        for circuit in self.circuits:
            if item == circuit.ID:
                return circuit
        raise KeyError("There is no such circuit ID.")


class Capstone(Project):
    def __init__(self, **kwargs):
        if len(kwargs) == 3:
            ID = kwargs["ID"]
            participants = kwargs["participants"]
            circuits = kwargs["circuits"]
        else:
            ID = kwargs["project"].ID
            participants = kwargs["project"].participants
            circuits = kwargs["project"].circuits
        super().__init__(ID, participants, circuits)
        for student in self.participants:
            if student.level is not Level.Senior:
                raise ValueError("Not all students are seniors!")


if __name__ == "__main__":

    student1 = Student("001", "Peter", "Parker", Level.Freshman)
    student2 = Student("002", "John", "Smith", Level.Senior)
    student3 = Student("003", "Amy", "Reynolds", Level.Senior)
    # student1 = Student("001", "Peter", "Parker", "Freshman")
    print(student1)
    print()
    comp1 = Component("123-456", ComponentType.Resistor, 2.4733)
    comp2 = Component("453-782", ComponentType.Capacitor, 1.715)
    comp3 = Component("348-387", ComponentType.Resistor, 2.86)
    comp4 = Component("787-342", ComponentType.Inductor, 3.50)
    # comp5 = Component("787-342", "Inductor", 3.50)
    print(comp1, comp2, comp3, comp4)
    print()
    comp_set = set()
    comp_set.add(comp1)
    comp_set.add(comp3)
    comp_set.add(comp4)
    comp_set2 = {comp1, comp3, comp4}
    circuit1 = Circuit("c-52346", comp_set)
    circuit2 = Circuit("c-13956", comp_set2)
    print(circuit1)
    print(circuit2)
    print(circuit1 == circuit2)
    print(circuit1.getByType(ComponentType.Resistor))
    # print(circuit1.getByType("Resistor"))
    circuit1 += comp2
    print(circuit1)
    circuit1 -= comp4
    print(circuit1)
    print(comp1 in circuit1)
    print(comp4 in circuit1)
    # print("comp4" in circuit1)
    print(circuit1 < circuit2)
    print(circuit1 == circuit2)
    print(circuit1 > circuit2)
    # print(circuit1 > "circuit2")
    print()
    print("Project tests")
    project1 = Project("38753067-e3a8-4c9e", [student1, student2, student3], [circuit2])
    project2 = Project("38346836-e3a8-4c9e", [student2, student3], [circuit1, circuit2])
    print(project1)
    print(project2)
    print(circuit2 in project1)
    print(comp2 in project1)
    print(student1 in project2)
    project1 += circuit1
    print(project1)
    project1 -= circuit2
    print(project1)
    print(project2["c-52346"])
    # print(project2[circuit1])
    # cap1 = Capstone(project1)
    # print(cap1)
    cap2 = Capstone(project=project2)
    print(cap2)
    cap2 = Capstone(ID="38346836-e3a8-4c9e", participants=[student2, student3], circuits=[circuit1, circuit2])
    print(cap2)


