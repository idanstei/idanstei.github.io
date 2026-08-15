# frozen_string_literal: true

require "al_cookie"

module AlCookie
  class << self
    alias_method :render_setup_script_without_consent_fix, :render_setup_script

    def render_setup_script(context)
      render_setup_script_without_consent_fix(context).sub(
        "onFirstConsent: function (consentData)",
        "onConsent: function (consentData)"
      )
    end
  end
end