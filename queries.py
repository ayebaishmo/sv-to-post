CREATE_TITANIC_TABLE = '''
    CTREATE TABLE IF NOT EXITS titanic_table
    ("Survived" INT,
    "Pclass" INT, 
    "Name" VARCHAR(200),
    "Sex" VARCHAR(200),
    "Age" REAL,
    "Siblings/Spouses Aboard" INT,
    "Parents/Children Aboard" INT,
    "Fare" REAL
    )
    '''