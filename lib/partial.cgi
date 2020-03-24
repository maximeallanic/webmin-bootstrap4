#
#Copyright 2020 Allanic.me ISC License License
#For the full copyright and license information, please view the LICENSE
#file that was distributed with this source code.
#Created by Maxime Allanic <maxime@allanic.me> at 22/03/2020
#

sub get_current_user_config
{
    our ($___user) =
      grep {$_->{'name'} eq $base_remote_user} &acl::list_users();
    return $___user;
}

sub print_menu_opener {
	print '<ul class="nav flex-column">' . "\n";
}

sub print_menu_category {
	local ($category, $label) = @_;
	use feature qw(switch);
	given($category) {
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
	print '<li class="nav-item">' . "\n";
        print '<button class="nav-link d-flex justify-content-between btn collapsed" data-open="#' . $category . '" data-toggle="collapse" href="#' . $category . '" role="button" aria-expanded="false" aria-controls="' . $category . '">' . "\n";
            print '<span>';
                print '<i class="fa fa-fw mr-2 ' . $icon . '"></i>';
                print '<span class="aside-text mx-auto">' . $label . '</span>';
            print '</span>';
            print '<span class="aside-arrow ml-1"><i class="fa fa-angle-right"></i></span>';
		print '</button>' . "\n";
	print '</li>' . "\n";
}

sub print_menu_closer {
	print '</ul>' . "\n";
}

sub print_sub_category_opener {
	local ($id) = @_;
	print '<div class="nav flex-nowrap flex-column mb-2 collapse" id="'.$id.'">' . "\n";
}

sub print_sub_category {
	local ($link, $label, $target) = @_;
	print '<span class="nav-item">' . "\n";
		print '<a class="nav-link btn text-left" href="' . $link .'" target="' . $target . '">' . $label . '</a>' . "\n";
	print '</span>' . "\n";
}

sub print_sub_category_closer {
	print '</div>' . "\n";
}

sub print_menu_search {
	print '<form class="search-aside" role="search" action="webmin_search.cgi" target="page-container">' . "\n";
	    print '<div class="form-group">' . "\n";
	        print '<input class="form-control" name="search" placeholder="Search" type="text">' . "\n";
	    print '</div>' . "\n";
	print '</form>' . "\n";
}

sub print_progressbar_colum {
	my ($xs, $sm, $percent, $label) = @_;
	use POSIX;
	$percent = ceil($percent);
	if ($percent < 75) {
		$class = 'success';
	} elsif ($percent < 90) {
		$class = 'warning';
	} else {
		$class = 'danger';
	}
	print '<div class="col-xs-' . $xs . ' col-sm-' . $sm . '">' . "\n";
	print '<div data-progress="' . $percent . '" class="progress progress-circle">' . "\n";
	print '<div class="progress-bar-circle progress-bar-' . $class . '">' . "\n";
	print '<div class="progress-bar-circle-mask progress-bar-circle-full">' . "\n";
	print '<div class="progress-bar-circle-fill"></div>' . "\n";
	print '</div>' . "\n";
	print '<div class="progress-bar-circle-mask progress-bar-circle-half">' . "\n";
	print '<div class="progress-bar-circle-fill"></div>' . "\n";
	print '<div class="progress-bar-circle-fill progress-bar-circle-fix"></div>' . "\n";
	print '</div>' . "\n";
	print '<div class="progress-bar-circle-inset">' . "\n";
	print '<div class="progress-bar-circle-title">' . "\n";
	print '<strong class="text-muted">' . $label . '</strong>' . "\n";
	print '</div>' . "\n";
	print '<div class="progress-bar-circle-percent">' . "\n";
	print '<span></span>' . "\n";
	print '</div>' . "\n";
	print '</div>' . "\n";
	print '</div>' . "\n";
	print '</div>' . "\n";
	print '</div>' . "\n";
}

sub get_col_num {
	my ($info, $max_col) = @_;
	my $num_col = 0;
	if ($info->{'cpu'}) { $num_col++; }
	if ($info->{'mem'}) {
		@m = @{$info->{'mem'}};
		if (@m && $m[0]) { $num_col++; }
		if (@m && $m[2]) { $num_col++; }
	}
	if ($info->{'disk_total'}) { $num_col++; }
	my $col = $max_col / ($num_col || 1);
	return $col;
}

sub print_table_row {
	local ($title, $content) = @_;
	print '<tr>' . "\n";
	print '<td><strong>' . $title . '</strong></td>' . "\n";
	print '<td>' . $content . '</td>' . "\n";
	print '</tr>' . "\n";
}