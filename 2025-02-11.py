from tortoise.expressions import F

from ballsdex.core.models import Ball, Economy, Regime, Special

await Ball.filter(wild_card__startswith="/static/uploads").update(
  wild_card=F("wild_card").replace("/static/uploads/", "")
)

await Ball.filter(collection_card__startswith="/static/uploads").update(
  collection_card=F("collection_card").replace("/static/uploads/", "")
)
