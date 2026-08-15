# frozen_string_literal: true

require "al_cookie"

module AlCookie
  class << self
    alias_method :render_setup_script_without_consent_fix, :render_setup_script

    def render_setup_script(context)
      script = render_setup_script_without_consent_fix(context)

      script = script.sub(
        "onFirstConsent: function (consentData)",
        "onConsent: function (consentData)"
      )

      script = script.sub(
        "var categories = consentData.categories || consentData;",
        'var categories = { analytics: window.CookieConsent.acceptedCategory("analytics") };'
      )

      script
    end
  end
end