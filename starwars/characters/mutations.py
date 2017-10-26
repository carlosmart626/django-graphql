import graphene

from .schemas import HumanCharacterNode
from .models import HumanCharacter


class HumanCharacterInputType(graphene.InputObjectType):
    """
    CarInsuranceApplicationType
    """
    human_id = graphene.Int(required=True)
    name = graphene.String()
    home_planet = graphene.String()


class UpdateHumanCharacter(graphene.Mutation):

    class Input:
        human_input = HumanCharacterInputType()

    human = graphene.Field(HumanCharacterNode)

    def mutate(self, args, context, info):
        try:
            human_data = args.get('human_input')
            print(human_data)
            human = HumanCharacter.objects.get(pk=human_data['human_id'])
            human.name = human_data['name']
            human.home_planet = human_data['home_planet']
            human.save()
            response = UpdateHumanCharacter(human=human)
        except Exception as e:
            return e
        return response
