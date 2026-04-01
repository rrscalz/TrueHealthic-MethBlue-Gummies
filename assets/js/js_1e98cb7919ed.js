
    (function() {
      var cdnOrigin = "https://cdn.shopify.com";
      var scripts = ["/cdn/shopifycloud/checkout-web/assets/c1/polyfills.CgsWKOqO.js","/cdn/shopifycloud/checkout-web/assets/c1/app.D9_I3YWy.js","/cdn/shopifycloud/checkout-web/assets/c1/dist-vendor.DBEA1s5W.js","/cdn/shopifycloud/checkout-web/assets/c1/browser.Doq0_afa.js","/cdn/shopifycloud/checkout-web/assets/c1/approval-scopes-FullScreenBackground.Ezw80F5b.js","/cdn/shopifycloud/checkout-web/assets/c1/shared-unactionable-errors.l7dIm5vW.js","/cdn/shopifycloud/checkout-web/assets/c1/actions-shop-discount-offer.D9iqJSzs.js","/cdn/shopifycloud/checkout-web/assets/c1/utilities-alternativePaymentCurrency.QrOHWByF.js","/cdn/shopifycloud/checkout-web/assets/c1/utils-proposal.CBJyNqYQ.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-useHasOrdersFromMultipleShops.DvkDzTn6.js","/cdn/shopifycloud/checkout-web/assets/c1/locale-en.CImBNg4j.js","/cdn/shopifycloud/checkout-web/assets/c1/page-OnePage.BtX0-s4r.js","/cdn/shopifycloud/checkout-web/assets/c1/Captcha-PaymentButtons.B8qIEQ7q.js","/cdn/shopifycloud/checkout-web/assets/c1/Menu-LocalPickup.CAj1Ljcn.js","/cdn/shopifycloud/checkout-web/assets/c1/timeout-trigger-MarketsProDisclaimer.C4mdU8Lq.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-NoAddressLocation.BgFo_CXC.js","/cdn/shopifycloud/checkout-web/assets/c1/shopPaySessionTokenStorage-Page.BVBh95YE.js","/cdn/shopifycloud/checkout-web/assets/c1/icons-OffsitePaymentFailed.CHQ58g4v.js","/cdn/shopifycloud/checkout-web/assets/c1/icons-ShopPayLogo.sTs24k5a.js","/cdn/shopifycloud/checkout-web/assets/c1/BuyWithPrimeChangeLink-VaultedPayment.Cm0m4L-e.js","/cdn/shopifycloud/checkout-web/assets/c1/DeliveryMacros-ShippingGroupsSummaryLine.4sCd3UXd.js","/cdn/shopifycloud/checkout-web/assets/c1/MerchandisePreviewThumbnail-StackedMerchandisePreview.Deep8xLw.js","/cdn/shopifycloud/checkout-web/assets/c1/Map-PickupPointCarrierLogo.DfqUXBkM.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks.B8CYcPQx.js","/cdn/shopifycloud/checkout-web/assets/c1/PostPurchaseShouldRender-AddDiscountButton.Bfu04HCy.js","/cdn/shopifycloud/checkout-web/assets/c1/graphql-RememberMeDescriptionText.oVuPHMfe.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-ShopPayOptInDisclaimer.D6sAU_Uc.js","/cdn/shopifycloud/checkout-web/assets/c1/utilities-MobileOrderSummary.BHaliVAZ.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-OrderEditVaultedDelivery.DMEP-qAf.js","/cdn/shopifycloud/checkout-web/assets/c1/captcha-SeparatePaymentsNotice.DNOa6cR5.js","/cdn/shopifycloud/checkout-web/assets/c1/StockProblems-StockProblemsLineItemList.BxqBixb4.js","/cdn/shopifycloud/checkout-web/assets/c1/redemption-useShopCashCheckoutEligibility.2sPYElmm.js","/cdn/shopifycloud/checkout-web/assets/c1/negotiated-ShipmentBreakdown.CkcCGLo0.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-MerchandiseModal.DonP7uY6.js","/cdn/shopifycloud/checkout-web/assets/c1/utilities-shipping-options.eKzNtGLN.js","/cdn/shopifycloud/checkout-web/assets/c1/graphql-DutyOptions.CB2uZcfp.js","/cdn/shopifycloud/checkout-web/assets/c1/DeliveryInstructionsFooter-ShippingMethodSelector.CHoLjLBX.js","/cdn/shopifycloud/checkout-web/assets/c1/hooks-SubscriptionPriceBreakdown.C4UJtk2w.js","/cdn/shopifycloud/checkout-web/assets/c1/component-RuntimeExtension.Dtj4Yxpb.js","/cdn/shopifycloud/checkout-web/assets/c1/DatePicker-AnnouncementRuntimeExtensions.D14FSCv1.js","/cdn/shopifycloud/checkout-web/assets/c1/standard-rendering-extension-targets.BbJAlOOF.js","/cdn/shopifycloud/checkout-web/assets/c1/esm-browser-v4.BKrj-4V8.js","/cdn/shopifycloud/checkout-web/assets/c1/ExtensionsInner.CYcCQ-jH.js","/cdn/shopifycloud/checkout-web/assets/c1/adapter-useShopPayNewSignupLoginExperiment.Mq5K5PCN.js"];
      var styles = ["/cdn/shopifycloud/checkout-web/assets/c1/assets/app.au8IBghB.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/FullScreenBackground.DQj8kWSJ.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/useHasOrdersFromMultipleShops.C8qHGRSx.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/OnePage.DRixGFzP.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/LocalPickup.BhtheElV.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/AddDiscountButton.oEoBAbtG.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/MobileOrderSummary.Cko1fUoG.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/OrderEditVaultedDelivery.CSQKPDv7.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/NoAddressLocation.BrcQzLuH.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/DutyOptions.LcqrKXE1.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/VaultedPayment.OxMVm7u-.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/PickupPointCarrierLogo.cbVP6Hp_.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/Page.BYM12A8B.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/OffsitePaymentFailed.CpFaJIpx.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/StackedMerchandisePreview.D6OuIVjc.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/ShippingMethodSelector.B0hio2RO.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/SubscriptionPriceBreakdown.BSemv9tH.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/RuntimeExtension.DWkDBM73.css","/cdn/shopifycloud/checkout-web/assets/c1/assets/AnnouncementRuntimeExtensions.V0VYEO4K.css"];
      var fontPreconnectUrls = [];
      var fontPrefetchUrls = [];
      var imgPrefetchUrls = ["https://cdn.shopify.com/s/files/1/0705/6405/3149/files/Healthic-Logo-Bigger-Top-_-Bottom_x320.png?v=1743439755"];

      function preconnect(url, callback) {
        var link = document.createElement('link');
        link.rel = 'dns-prefetch preconnect';
        link.href = url;
        link.crossOrigin = '';
        link.onload = link.onerror = callback;
        document.head.appendChild(link);
      }

      function preconnectAssets() {
        var resources = [cdnOrigin].concat(fontPreconnectUrls);
        var index = 0;
        (function next() {
          var res = resources[index++];
          if (res) preconnect(res, next);
        })();
      }

      function prefetch(url, as, callback) {
        var link = document.createElement('link');
        if (link.relList.supports('prefetch')) {
          link.rel = 'prefetch';
          link.fetchPriority = 'low';
          link.as = as;
          if (as === 'font') link.type = 'font/woff2';
          link.href = url;
          link.crossOrigin = '';
          link.onload = link.onerror = callback;
          document.head.appendChild(link);
        } else {
          var xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onloadend = callback;
          xhr.send();
        }
      }

      function prefetchAssets() {
        var resources = [].concat(
          scripts.map(function(url) { return [url, 'script']; }),
          styles.map(function(url) { return [url, 'style']; }),
          fontPrefetchUrls.map(function(url) { return [url, 'font']; }),
          imgPrefetchUrls.map(function(url) { return [url, 'image']; })
        );
        var index = 0;
        function run() {
          var res = resources[index++];
          if (res) prefetch(res[0], res[1], next);
        }
        var next = (self.requestIdleCallback || setTimeout).bind(self, run);
        next();
      }

      function onLoaded() {
        try {
          if (parseFloat(navigator.connection.effectiveType) > 2 && !navigator.connection.saveData) {
            preconnectAssets();
            prefetchAssets();
          }
        } catch (e) {}
      }

      if (document.readyState === 'complete') {
        onLoaded();
      } else {
        addEventListener('load', onLoaded);
      }
    })();
  