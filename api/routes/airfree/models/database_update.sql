update airfree
set
    id=:coin_id,
    name=:name,
    image_path=:image_path,
    site=:site,
    coin_nft_link=:coin_nft_link,
    whitepaper=:whitepaper,
    coin_marketcap_link=:coin_marketcap_link,
    total_supply=:total_supply,
    is_active=:is_active,
    platform=:platform
where id=:coin_id;