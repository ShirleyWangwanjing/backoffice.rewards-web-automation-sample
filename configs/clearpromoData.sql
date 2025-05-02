USE iHerb_Shop
SELECT TC.CampaignId, PromoId, TC.CreatedBy, TC.CampaignName INTO #TCombinedRewardPromo FROM iherb_shop.shopservice.TBL_RewardCampaign TC INNER JOIN iherb_shop.shopservice.TBL_RewardCampaignPromo TCP ON TC.CampaignId = TCP.CampaignId INNER JOIN iherb_shop.shopservice.TBL_Promo TP ON TCP.PromoId = TP.id WHERE CreatedBy = 'test-brm.campign-edi'
DELETE FROM iherb_shop.shopservice.TBL_RewardCampaignPromo WHERE CampaignId IN (SELECT DISTINCT CampaignId FROM #TCombinedRewardPromo)
DELETE FROM iherb_shop.shopservice.TBL_RewardCampaign WHERE CampaignId IN (SELECT DISTINCT CampaignId FROM #TCombinedRewardPromo)
DELETE FROM iherb_shop.shopservice.TBL_PromoRewards WHERE PromoID IN (SELECT DISTINCT PromoId FROM #TCombinedRewardPromo)
DELETE FROM iherb_shop.shopservice.TBL_PromoStore WHERE PromoId IN (SELECT DISTINCT PromoId FROM #TCombinedRewardPromo)
DELETE FROM iherb_shop.shopservice.TBL_Promo WHERE id IN (SELECT DISTINCT PromoId FROM #TCombinedRewardPromo)

