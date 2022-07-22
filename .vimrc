set number
set ruler
set expandtab tabstop=4 softtabstop=4
set autoindent cindent smartindent
set belloff=all
set backspace=2
syntax on

set laststatus=2
set t_Co=256

set mouse=a
set showtabline=2
set noshowmode
set showcmd
set guioptions=
set guifont=YaHei\ Consolas\ Hybrid:h14

call plug#begin()
Plug 'Lokaltog/vim-powerline' 
Plug 'nathanaelkane/vim-indent-guides'
Plug 'preservim/nerdtree'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'kien/ctrlp.vim'
call plug#end()

let g:indent_guides_enable_on_vim_startup = 1
let g:coc_global_extensions = ['coc-json', 'coc-css', 'coc-html', 'coc-pyright', 'coc-clangd', 'coc-snippets', 'coc-git', 'coc-translator']
let laststatus = 2

" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()

let g:Powerline_colorscheme='solarized256'
let g:ctrlp_map = '<c-p>'
let g:ctrlp_cmd = 'CtrlP'

set wildignore+=*/tmp/*,*.so,*.swp,*.zip     " MacOSX/Linux
set wildignore+=*\\tmp\\*,*.swp,*.zip,*.exe  " Windows

let g:ctrlp_custom_ignore = '\v[\/]\.(git|hg|svn)$'
let g:ctrlp_custom_ignore = {
  \ 'dir':  '\v[\/]\.(git|hg|svn)$',
  \ 'file': '\v\.(exe|so|dll|swp)$',
  \ 'link': 'some_bad_symbolic_links',
  \ }

let g:ctrlp_user_command = 'find %s -type f'        " MacOSX/Linux

" popup
nmap <Leader>t <Plug>(coc-translator-p)
vmap <Leader>t <Plug>(coc-translator-pv)
" echo
nmap <Leader>e <Plug>(coc-translator-e)
nmap <Leader>e <Plug>(coc-translator-ev)
" replace
nmap <Leader>r <Plug>(coc-translator-r)
nmap <Leader>r <Plug>(coc-translator-rv)

colo darcula
set nowrap

