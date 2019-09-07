from django.test import TestCase

from shop.factories import OrderProductRelationFactory
from .factories import TicketTypeFactory
from .models import ShopTicket


class TicketTests(TestCase):

    def test_correct_token_and_badge_token_are_different(self):

        ticket_type = TicketTypeFactory()

        orp = OrderProductRelationFactory()
        shop_ticket = ShopTicket.objects.create(
            ticket_type=ticket_type,
            product=orp.product,
            order=orp.order,
        )

        self.assertNotEqual(shop_ticket.token, shop_ticket.badge_token)
        self.assertEqual(shop_ticket.token, shop_ticket._get_token())
        self.assertEqual(shop_ticket.badge_token, shop_ticket._get_badge_token())

