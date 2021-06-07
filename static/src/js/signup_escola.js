odoo.define('auth_signup.signup_escola', function (require) {
    'use strict';

var base = require('web_editor.base');

base.ready().then(function() {
    // Disable 'Sign Up' button to prevent user form continuous clicking
    if ($('.oe_signup_form').length > 0) {
        $('.oe_signup_form').on('submit', function () {
            $('.o_signup_btn').attr('disabled', 'disabled');
            $('.o_signup_btn').prepend('<i class="fa fa-refresh fa-spin"/> ');
        });
    }

    if ($('.oe_signup_form').length> 0) {
        var state_options = $("select[name='state_id']:enabled option:not(:first)");
        $('.oe_signup_form').on('change', "select[name='country_id']", function () {
            var select = $("select[name='state_id']");
            state_options.detach();
            var displayed_state = state_options.filter("[data-country_id="+($(this).val() || 0)+"]");
            var nb = displayed_state.appendTo(select).show().size();
            select.parent().toggle(nb>=1);
        });
        $('.oe_signup_form').find("select[name='country_id']").change();
    }
});

});
