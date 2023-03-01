from Components.Ads.Photo.ImageAd import ImageAd
from Components.Ads.Text.TextAd import TextAd
from Components.Ads.Decorator.TextAdsDecorator import TextAdsDecorator
from Components.Ads.Decorator.ImageAdsDecorator import ImageAdsDecorator, GoogleImageAdDecorator, MetaImageAdDecorator
from Components.Ads.Decorator.AdsChannelDecorator import AdsChannelDecorator

if __name__ == '__main__':
    text_ad = TextAd(text='Hello text ad content')
    image_ad = ImageAd(image_uri='A file path or uri should be here')

    # Example for ad classes without decorators
    print(f'Example 1 - text ad decorator output:')
    print(TextAdsDecorator(text_ad).get_content())
    print(f'Example 1 - image ad decorator output:')
    print(ImageAdsDecorator(image_ad).get_content())
    print('-'*20)

    # Example for apply multiple decorators for ad classes
    print(f'Example 2 - Google Ads with text ad decorator output:')
    print(AdsChannelDecorator(TextAdsDecorator(text_ad), channel="Google Ads").get_ad_channel())
    print(f'Example 2 - Meta Ads with text ad decorator output:')
    print(AdsChannelDecorator(TextAdsDecorator(text_ad), channel="Meta Ads").get_ad_channel())
    print('-' * 20)

    # Example for apply multiple decorators with different order
    print(f'Example 3 - image ads decorator output:')
    print(AdsChannelDecorator(ImageAdsDecorator(image_ad), channel="Youtube Ads").get_content())
    print(f'Example 3 - exchange decorators output:')
    print(ImageAdsDecorator(AdsChannelDecorator(image_ad, channel="Instagram Ads")).get_content())
    print('-' * 20)

    # Example for inherit decorator class to setting different behavior, such as photo size limitation
    print(f'Example 4 - inherit image ads decorator output:')
    google_image_ads = GoogleImageAdDecorator(AdsChannelDecorator(image_ad, channel='Google Ads'))
    # assume google image ads size limitation with: 320 <= width <= 1920, 480 <= height <= 1080
    google_image_ads.width = 2560.0
    google_image_ads.height = 1440.0
    print(f'Over Google Image Ads size limitation')
    print(google_image_ads.get_content())


