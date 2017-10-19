from django.test import TestCase

from api.schemas import schema


class GraphQLTests(TestCase):
    """
    This TestCase auth.
    """

    @classmethod
    def setUpClass(cls):
        super(GraphQLTests, cls).setUpClass()
        cls.schema = schema
        cls.query_node = '''
            query{
              hello(name: "Carlos")
            }
        '''

    def test_query(self):
        result = self.schema.execute(self.query_node)
        self.assertNotEqual(result.errors, [])
