<script setup>
const query = ref('')
const selected = ref('hpml-view-for-user')
const tasks = ['hpml-view-for-user','hermes-joint-workspace','jev-integration','mcp-workspace','mow-mot-moit-mout','vps-clean-20-9-26']
const filtered = computed(() => tasks.filter(t => t.includes(query.value.toLowerCase())))
const items = [
 { label: 'Mục tiêu', summary: 'Biết mục tiêu, biết trạng thái để điều hành hiệu quả', slot: 'goal', defaultOpen: true },
 { label: 'Tiến độ', summary: '② Kế hoạch · Đang cùng User thiết kế UI', slot: 'progress' },
 { label: 'Tình trạng', summary: 'Đang thiết kế · Chờ User chỉnh bản phác thảo', slot: 'activity', defaultOpen: true },
 { label: 'Nội dung công việc', summary: 'HTML chính của công việc', slot: 'document' }
]
const stages = ['Tạo việc · Thống nhất mục tiêu','Thống nhất kế hoạch','Triển khai','Nghiệm thu theo mục tiêu']
</script>
<template>
 <div class="min-h-screen bg-white text-slate-900">
  <header class="border-b border-slate-200 px-6 py-3 flex items-center justify-between gap-3"><div class="flex items-center gap-4"><span class="font-semibold">INCOMEX</span><span class="text-slate-300">/</span><span class="text-sm text-slate-600">Knowledge</span><span class="text-slate-300">/</span><span class="text-sm font-medium">Task html view</span></div><UBadge color="gray" variant="soft">Bản phác thảo · Chưa nối dữ liệu</UBadge></header>
  <div class="px-6 py-5 max-w-[1600px] mx-auto">
   <div class="flex justify-between items-center mb-5 gap-4"><div><h1 class="text-xl font-semibold">Task html view</h1><p class="text-sm text-slate-500 mt-1">Mục tiêu rõ · Nắm tình trạng · Biết bước tiếp theo</p></div><UButton color="gray" variant="outline" disabled title="Bản phác thảo chưa kết nối GitHub">Cập nhật</UButton></div>
   <div class="task-layout grid grid-cols-1 gap-6 items-start">
    <aside class="min-w-0 lg:sticky lg:top-5">
     <UInput v-model="query" placeholder="Tìm công việc…" aria-label="Tìm công việc" size="lg" />
     <div class="flex items-center justify-between mt-4 mb-2"><h2 class="text-sm font-semibold">Công việc trong repo</h2><span class="text-xs text-slate-500">{{ filtered.length }} việc</span></div>
     <nav aria-label="Danh sách công việc" class="space-y-1">
      <UButton v-for="task in filtered" :key="task" :color="selected === task ? 'primary' : 'gray'" :variant="selected === task ? 'soft' : 'ghost'" block :ui="{ base: 'justify-start text-left' }" class="px-3 py-3 !justify-start" size="lg" @click="selected = task"><span class="min-w-0"><span class="block break-words font-medium">{{ task }}</span><span class="block mt-1 text-xs font-normal text-slate-500">{{ task === 'hpml-view-for-user' ? 'Kế hoạch · Đang thiết kế UI với User' : 'Chưa nạp tình trạng trong bản phác thảo' }}</span></span></UButton>
      <p v-if="!filtered.length" class="p-3 text-sm text-slate-500">Không có công việc khớp tên.</p>
     </nav><p class="mt-5 pt-4 border-t text-xs text-slate-400">Nguồn danh sách: incomex-workspace / work</p>
    </aside>
    <main class="min-w-0">
     <div class="mb-4"><h2 class="text-xl font-semibold break-words">{{ selected }}</h2><p class="text-xs text-slate-500 mt-2">{{ selected === 'hpml-view-for-user' ? 'Đang thiết kế giao diện · Chưa triển khai' : 'Chỉ minh họa việc chuyển công việc' }}</p></div>
     <UAccordion v-if="selected === 'hpml-view-for-user'" :items="items" multiple :ui="{ wrapper: 'flex flex-col w-full gap-3', container: 'border border-slate-200 rounded-lg overflow-hidden', item: { padding: 'px-4 pb-4 pt-1', color: 'text-slate-700' } }">
      <template #default="{ item, open }"><UButton color="gray" variant="ghost" class="w-full rounded-none p-4" :ui="{ base: 'justify-between text-left' }"><span class="min-w-0"><span class="block text-sm font-semibold text-slate-900">{{ item.label }}</span><span class="block text-xs font-normal text-slate-500 mt-1">{{ item.summary }}</span></span><span class="ml-3 text-slate-400 text-lg" aria-hidden="true">{{ open ? '−' : '+' }}</span></UButton></template>
      <template #goal><p class="text-base leading-relaxed">View dễ nhìn cho User để biết mục tiêu, biết trạng thái, giúp điều hành hiệu quả.</p><p class="mt-3 text-sm font-medium">Lắp ráp tối đa, hạn chế code mới tối đa.</p><p class="mt-3 text-xs text-slate-500">Theo yêu cầu User trong phiên thiết kế này. Bản chạy thật đọc mục tiêu từ nguồn GitHub.</p></template>
      <template #progress><ol class="space-y-3"><li v-for="(stage, i) in stages" :key="stage" class="flex items-start gap-3"><UBadge :color="i === 1 ? 'primary' : 'gray'" :variant="i === 1 ? 'solid' : 'soft'">{{ i + 1 }}</UBadge><div><p :class="i === 1 ? 'font-semibold text-violet-700' : ''">{{ stage }}</p><p v-if="i === 1" class="text-xs text-slate-500 mt-1">Đang chỉnh bố cục cùng User</p><p v-if="i === 0" class="text-xs text-slate-500 mt-1">User đã đồng ý mục tiêu và khung 2 cột</p></div></li></ol><p class="text-xs text-slate-500 mt-4">Khi điều chỉnh, ghi rõ ngay tại giai đoạn tương ứng.</p></template>
      <template #activity><div class="divide-y divide-slate-100"><div class="py-3"><p class="text-xs font-medium text-slate-500">CHAT · Ý KIẾN GẦN NHẤT</p><p class="mt-1 text-sm">Chưa nạp dữ liệu</p><p class="text-xs text-slate-400 mt-1">GPT Chat · Claude Chat · Hermes Chat</p></div><div class="py-3"><p class="text-xs font-medium text-slate-500">THỰC HIỆN · KẾT QUẢ GẦN NHẤT</p><p class="mt-1 text-sm">Chưa nạp dữ liệu</p><p class="text-xs text-slate-400 mt-1">Codex / GPT Work · Claude Cowork · Claude Code CLI</p></div><div class="py-3 flex justify-between gap-4 text-sm"><span class="text-slate-500">Ai đang làm?</span><span>Chưa có tín hiệu</span></div><div class="pt-3 text-sm"><span class="font-medium">Tiếp theo: </span>User xem và chỉnh bản phác thảo</div></div></template>
      <template #document><p class="text-sm leading-relaxed">Nội dung HTML chính của công việc hiển thị tại đây. Khi cần đọc rộng hơn, thu gọn Mục tiêu, Tiến độ và Tình trạng ở phía trên.</p><p class="mt-3 text-xs text-slate-500">Bản này chỉ thử bố cục và thao tác, chưa nạp nội dung các công việc khác.</p></template>
     </UAccordion>
     <UAlert v-else color="gray" title="Chưa nạp nội dung" description="Bản phác thảo tập trung vào hpml-view-for-user. Chọn lại công việc đó để thử mở và thu gọn các mục." />
    </main>
   </div>
  </div>
 </div>
</template>
<style>
/* Knowledge: 4 equal tracks, 24px gaps. Sidebar = 1.5 times its original track. */
@media(min-width:1024px){.task-layout{grid-template-columns:calc((100% - 72px)/4 * 1.5) minmax(0,1fr)}}
</style>
