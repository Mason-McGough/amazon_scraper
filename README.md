# amazon_scraper spike project

## frontend server
`yarn dev`

frontend requires `.env` with variable `VITE_PROXY_API_KEY`. this key is provided by ScraperAPI.
## scraper server
`scrapyrt`


# Amazon Seller Partner API
## Definitions
*Seller Central*: Seller Central is the portal for accessing your Amazon seller account. It’s a one-stop shop for effectively managing sales, and your go-to resource for selling in Amazon’s store.

*Seller Central Partner Network*: Amazon-approved third-party software and services to automate, manage, and grow your business.

*Software Partners*: Find automated solutions to manage and grow your business from our Software Partners. Many apps focus on automating previously time-consuming and tedious daily tasks like product research, filling out tax forms, or building customized reports.

*Service Partners*: Explore a directory of third-party services from Service Partners across the globe. From *shooting great images* for your products to improving your chances of increasing sales on Amazon, Service Partners can help you with every step of selling online.

* *Selling partner:* A selling partner can be a seller or a vendor.
* *Seller:* A seller lists and sells their own goods on Amazon’s retail website. After an item is sold, it is either (1) directly fulfilled by the seller using inventory managed by the seller, or (2) fulfilled through the Fulfillment by Amazon (FBA) program, using the seller’s FBA inventory.
* *Vendor:* A vendor supplies the inventory that is sold by Amazon on Amazon’s retail website. There are two main types of vendors: Retail procurement vendors and Direct fulfillment vendors.
	* *Retail procurement vendor:* A retail procurement vendor sells inventory to Amazon and ships it to Amazon’s fulfillment centers. Amazon then sells and ships the inventory to customers who make purchases on Amazon’s retail website. A retail procurement vendor can be a brand owner or a distributor. In some cases they manage the listings of the products that they supply to Amazon.
	* *Direct fulfillment vendor:* A direct fulfillment vendor ships orders to customers on Amazon’s behalf. After a customer makes a purchase from Amazon on Amazon’s retail website, the direct fulfillment vendor ships the order directly to the customer.
* *Public application:* An application that is publicly available and is authorized by a selling partner.
* *Private application:* An application that is available only to your organization and is self-authorized.
* *Public developer:* A developer that builds and offers publicly available applications that are used by other companies.
* *Private developer:* A developer that builds application(s) that integrate their own company with Amazon APIs.


*What’s the difference between an app and a service?*
Apps are software that integrates with Amazon Marketplace Web Services or Selling Partner APIs to automate and scale your business. Services augment in-house capabilities by providing things like storage and international shipping.

*I’m a new developer or service provider. How can I be included Seller Central Partner Network?*
For developers, please visit  [developer.amazonservices.com](https://developer.amazonservices.com/?ref_=sdus_soa_resources_faq_dev&initialSessionID=147-9990381-0315106&ld=ELUSSOA-duckduckgo.com&ldStackingCodes=SCUSWPDirect%3EELUSSOA-sellercentral.amazon.com%3EELUSSOA-duckduckgo.com)  for more information. For service providers, please  [contact us via email](mailto:spn-newinquire@amazon.com)  for more information.


[Legal Agreement to use Seller API](https://sellercentral.amazon.com/mws/static/agreement?locale=en_US)
[Acceptable Use Policy](https://sellercentral.amazon.com/mws/static/policy?documentType=AUP&locale=en_US)
[Data Protection Policy](https://sellercentral.amazon.com/mws/static/policy?documentType=DPP&locale=en_US)


*Do I need a Professional Selling Account to register as a Selling Partner API developer?*
Yes, only Professional Selling Accounts can register to develop or integrate with Selling Partner API. Individual accounts are not eligible. You can upgrade your account to a professional plan at any time. You can view your selling plan type and the marketplace information under “Your Services” in  [Account info](https://sellercentral.amazon.com//hz/sc/account-information) .

*Do I need to have a professional selling account to use Sandbox endpoint?*
Yes, Making sandbox calls to the SP API is identical to making production calls except you direct the calls to the SP API sandbox endpoints. Calling the sandbox endpoints returns static, mocked responses for all Selling Partner APIs. Sandbox endpoint allows you to test your applications without affecting production data or triggering real-world events.


[Registering as a developer](https://developer-docs.amazon.com/sp-api/docs/registering-as-a-developer)
You must register as a Selling Partner API developer before you can  [register your Selling Partner API application](https://developer-docs.amazon.com/sp-api/docs/registering-your-application) . The procedure for registering as a developer varies slightly depending on the type of application that you plan to create. Developer applications are grouped into three types:
* *All public applications.* Applications that are publicly available and are authorized by sellers or by vendors using OAuth.
* *Private seller applications.* Applications for sellers that are available only to your organization, and are self-authorized.
* *Private vendor applications.* Applications for vendors that are available only to your organization, and are self-authorized.

### To register as a public developer (for all public applications)
[Getting Started Videos](https://www.youtube.com/playlist?list=PLyrrqKCT7jFKENJO9n_Y68-5o2GZLgLUU)
1 Sign into Seller Central using the credentials that you want to associate with your developer account.
2 From the *Partner Network* menu, choose *Develop Apps*.
3 If you have not yet completed a developer profile for this selling account, select *Proceed to Developer Profile*. Otherwise, select the *View profile* link.
4 Complete the form. From the *Data Access* section dropdown box, choose *Public Developer: I build and offer publicly available applications that are used by other companies”*.
