set t_Co=256
set nocompatible
set backspace=indent,eol,start

if has("vms")
  set nobackup		" do not keep a backup file, use versions instead
else
  set backup		" keep a backup file
endif

set history=50		" keep 50 lines of command line history
set ruler		" show the cursor position all the time
set showcmd		" display incomplete commands
set incsearch " do incremental searching
set expandtab
set laststatus=2
if has("gui_running")
	set guifont=consolas:h14
	set guioptions=
	colo solarized
	if has("win32")
		set noerrorbells visualbell t_vb=
		autocmd GUIEnter * set visualbell t_vb=
		set t_vb=
	endif
	else
		colo torte
		set noerrorbells visualbell t_vb=
endif

set list
set listchars=tab:>-,trail:~,extends:>,precedes:<,space:·


set tabstop=4
set mouse=
set encoding=utf-8
set number

set fileencodings=utf-8,utf-16,big5,gb2312,gbk,gb18030,euc-jp,euc-kr,latin1

set noautoindent
filetype indent off
syntax on


map <F2> :call SwitchTextBinaryMode()<CR>
map! <F2> <Esc>:call SwitchTextBinaryMode()<CR>
function SwitchTextBinaryMode()
		if (&binary == 0)
			set binary
			set noeol
			echo "Switch to binary mode."
		else
			set nobinary
			set eol
			echo "Switch to text mode."
		endif
endfunction



set cursorline
hi CursorLine cterm=none ctermbg=DarkGray
set cursorcolumn
hi Cursorcolumn cterm=none ctermbg=DarkGray

function IsBinary()
    if (&binary == 0)
        return ""
    else
        return "[Binary]"
    endif
endfunction

function FileSize()
    let bytes = getfsize(expand("%:p"))
    if bytes <= 0
        return "[Empty]"
    endif
    if bytes < 1024
        return "[" . bytes . "B]"
    elseif bytes < 1048576
        return "[" . (bytes / 1024) . "KB]"
    else
        return "[" . (bytes / 1048576) . "MB]"
    endif
endfunction



set statusline=%#filepath#[%{expand('%:t')}]%#filetype#[%{strlen(&fenc)?&fenc:&enc},\ %{&ff},\ %{strlen(&filetype)?&filetype:'plain'}]%#filesize#%{FileSize()}%{IsBinary()}%=%#position#%c,%l/%L\ [%3p%%]



set showcmd
set showmode
set nowrap

set guicursor=n-v-c:block-Cursor

let &guicursor = substitute(&guicursor, 'n-v-c:', '&blinkon0-', '')

" Use a line cursor within insert mode and a block cursor everywhere else.
"
" Reference chart of values:
"   Ps = 0  -> blinking block.
"   Ps = 1  -> blinking block (default).
"   Ps = 2  -> steady block.
"   Ps = 3  -> blinking underline.
"   Ps = 4  -> steady underline.
"   Ps = 5  -> blinking bar (xterm).
"   Ps = 6  -> steady bar (xterm).
let &t_SI = "\e[6 q"
let &t_EI = "\e[2 q"



