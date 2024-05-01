RDBMS Using Relations and Functions

Data Structure and Representation in Python
In the provided Python program, the data is represented using lists and dictionaries, which map to a simplified form of tables in RDBMS:

Lists (roll_no, names, dob, yos) represent columns in a relational database.
Dictionary (mapping) simulates a table by correlating each student's roll number with their respective details (name, date of birth, year of study).
Mapping and Data Relations
In RDBMS, relations describe the association between different tables. These relations can be characterized by the function mapping used:

Many-to-One: In the context of your dataset, if we consider the relation between names and dob or yos, it represents a many-to-one relationship, because multiple names might map to one date of birth or year of study (theoretically speaking if the dataset had repeating dates or years). However, in your dataset, each roll number (unique identifier) maps to one set of attributes (Names, DOB, YOS), establishing a clear many-to-one relationship from roll numbers to other attributes.
One-to-Many: This relation is illustrated if you consider any attribute as a key that maps to multiple values. In the given dataset, each key (like DOB) could theoretically be associated with multiple names (one-to-many) if multiple students share the same birthdate.
Functions Used in the Program
Functions in this context refer to the operations performed on the data:

Sorting: The DataFrame is sorted based on different attributes (index, names, dob, yos), which simulates SQL operations like ORDER BY.
Mapping: Using Python dictionaries to map roll numbers to student attributes simulates creating relations between different entities in a database.
DataFrame Creation and Manipulation: These operations are akin to SQL queries that select and display data from tables.
Conclusion
In RDBMS, data integrity and structured relationships between entities (tables) ensure that data is stored efficiently and can be accessed quickly through various relational operations. The Python script simulates a simple RDBMS model where data relationships are defined using basic data structures (lists and dictionaries) to demonstrate how relational data operations can be conceptualized and performed outside of a traditional database environment.

This report outlines the fundamental concepts of RDBMS using a Python program as an analog. While the program does not fully implement RDBMS features, it provides a basis for understanding relational data handling through procedural programming techniques.
