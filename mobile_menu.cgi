#############################################################################################################################
# BWTheme 0.9.5 (https://github.com/winfuture/Bootstrap3-Webmin-Theme) - (http://theme.winfuture.it)						#
# Copyright (c) 2015 Riccardo Nobile <riccardo.nobile@winfuture.it> and Simone Cragnolini <simone.cragnolini@winfuture.it>	#
# Licensed under GPLv3 License (https://github.com/winfuture/Bootstrap3-Webmin-Theme/blob/testing/LICENSE)					#
#############################################################################################################################

BEGIN { push(@INC, ".."); };
use WebminCore;
&ReadParse();
&init_config();
%text = &load_language($current_theme);
%gaccess = &get_module_acl(undef, "");
$charset = &get_charset();
$title = &get_html_framed_title();
&header($title);
print '<div id="wrapper" class="page">' . "\n";
print '<div class="container">' . "\n";
@cats = &get_visible_modules_categories();
$category = $in{'category'};
$row = 1;
if ($category eq '') {
	print '<div class="row menu-row" style="margin-top: 20px">' . "\n";
	foreach $cat (@cats) {
		&print_category_menu($cat->{'code'}, $in{$cat->{'code'}} ? 1 : 0, $cat->{'desc'});
	}
	print '</div>' . "\n";
} else {
	print '<div class="list-group" style="margin-top: 20px">' . "\n";
	foreach $cat (@cats) {
		next if ($cat->{'code'} ne $category);
		foreach my $module (@{$cat->{'modules'}}) {
			&print_category_link("$module->{'dir'}/", $module->{'desc'}, undef, undef, $module->{'noframe'} ? "_top" : "", );
		}
	}
	print '</div>' . "\n";
}
print '</div>' . "\n";

&footer();

sub print_category_menu {
local ($cat, $status, $label) = @_;
$label = $cat eq "others" ? $text{'left_others'} : $label;
use feature qw(switch);
given($cat){
  when('webmin') { $icon = 'fa-cog'; }
  when('usermin') { $icon = 'fa-cog'; }
  when('system') { $icon = 'fa-wrench'; }
  when('servers') { $icon = 'fa-rocket'; }
  when('other') { $icon = 'fa-file'; }
  when('net') { $icon = 'fa-shield'; }
  when('info') { $icon = 'fa-info'; }
  when('hardware') { $icon = 'fa-hdd-o'; }
  when('cluster') { $icon = 'fa-power-off'; }
  when('unused') { $icon = 'fa-puzzle-piece'; }
  when('mail') { $icon = 'fa-envelope'; }
  when('login') { $icon = 'fa-user'; }
  when('apps') { $icon = 'fa-rocket'; }
  default { $icon = 'fa-cog'; }
}
print '<div class="col-xs-6">' . "\n";
print '<div class="menu-col" style="background-color: #222; border-radius: 4px; margin: 0 auto 30px; width: 140px; height: 140px;">' . "\n";
print '<a class="menu-link" href="mobile_menu.cgi?category=' . $cat . '">' . "\n";
print '<div style="padding: 15px 10px;">' . "\n";
print '<i class="fa ' . $icon . ' fa-fw"></i>' . "\n";
print '<div style="margin-top: 6px;">' . $label . '</div>' . "\n";
print '</div>' . "\n";
print '</a>' . "\n";
print '</div>' . "\n";
print '</div>' . "\n";
}


sub print_category_link {
local ($link, $label, $image, $noimage, $target) = @_;
	$target ||= "page-container";
	print '<a class="list-group-item" target="' . $target . '" href="' . $link . '"> ' . $label . '</a>' . "\n";
}
